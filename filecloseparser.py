import sys
import re
from dataclasses import dataclass

from typing import Callable, Optional, TextIO

class FileCloseParser:
    def __init__(self, file: TextIO):
        self.source_code = file
        self.fstreams = []

        self.match_with_dec: Callable[[str], Optional[FileCloseParser.Fstream]] = FileCloseParser.declaration_matcher()

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
    def open_matcher():
        return lambda x: None

    @staticmethod
    def close_matcher():
        return lambda x: None

    # the actual parsing & checking stuff for fstream closing

    def walk_through_file(self) -> None:
        for line in self.source_code:
            # TODO: strip lines into individual statements
            self.process_line(line.strip())

    def process_line(self, line:str) -> None:
        if (fstream := self.match_with_dec(line)):
            self.fstreams.append(fstream)


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