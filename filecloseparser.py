import sys
import re
from dataclasses import dataclass

from typing import Callable, Optional, TextIO

class FileCloseParser:
    def __init__(self, file: TextIO):
        self.source_code = file
        self.fstreams = {}

        self.match_with_dec: Callable[[str], Optional[FileCloseParser.Fstream]] = FileCloseParser.declaration_matcher()
        self.match_with_open: Callable[[str], Optional[str]] = FileCloseParser.open_matcher()
        self.match_with_close: Callable[[str], Optional[str]] = FileCloseParser.close_matcher()

    @dataclass
    class Fstream:
        name: str
        opened: bool = False
        closed: bool = False

    # static methods that return a function that does some regex shih

    @staticmethod
    def declaration_matcher() -> Callable[[str], Optional["FileCloseParser.Fstream"]]:
        pattern = re.compile(
            r"""
            (?:(?:const|static|extern|mutable|register)\s+)*
            (?:std::)?
            (?:f|if|of)stream
            \s+
            (?P<name>[A-Za-z_]\w*)
            \s*
            (?:
                (?P<init>\([^;]*\)|\{[^;]*\})\s*
            )?
            ;?
            """,
            re.VERBOSE,
        )

        def matcher(statement: str) -> Optional[FileCloseParser.Fstream]:
            match = pattern.fullmatch(statement)
            if not match:
                return None

            init = match.group("init")
            return FileCloseParser.Fstream(
                name=match.group("name"),
                opened=init is not None and bool(re.search(r"[^(){}\s]", init)),
            )

        return matcher

    @staticmethod
    def open_matcher() -> Callable[[str], Optional[str]]:
        pattern = re.compile(
            r"""
            (?P<name>[A-Za-z_]\w*)
            \s*
            \.
            \s*
            open
            \s*
            \([^;]*\)
            \s*
            ;?
            """,
            re.VERBOSE,
        )

        def matcher(statement: str) -> Optional[str]:
            match = pattern.fullmatch(statement)
            if not match:
                return None

            return match.group("name")

        return matcher

    @staticmethod
    def close_matcher() -> Callable[[str], Optional[str]]:
        pattern = re.compile(
            r"""
            (?P<name>[A-Za-z_]\w*)
            \s*
            \.
            \s*
            close
            \s*
            \(
            \s*
            \)
            \s*
            ;?
            """,
            re.VERBOSE,
        )

        def matcher(statement: str) -> Optional[str]:
            match = pattern.fullmatch(statement)
            if not match:
                return None

            return match.group("name")

        return matcher

    # the actual parsing & checking stuff for fstream closing

    def walk_through_file(self) -> None:
        for line in self.source_code:
            # TODO: strip lines into individual statements
            self.process_statement(line.strip())

    def process_statement(self, statement:str) -> None:
        if (fstream := self.match_with_dec(statement)):
            self.fstreams[fstream.name] = fstream

        elif (fstream_name := self.match_with_open(statement)):
            self.fstreams[fstream_name].opened = True
        
        elif (fstream_name := self.match_with_close(statement)):
            self.fstreams[fstream_name].closed = True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {str(sys.argv[0])} filepath")
        sys.exit(2)

    result = None
    with open(sys.argv[1]) as f:
        parser = FileCloseParser(f)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)