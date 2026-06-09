import sys
from io import TextIOWrapper
import re
from dataclasses import dataclass

from typing import Callable, Optional

class FileCloseParser:
    def __init__(self, file: TextIOWrapper):
        self.source_code = file
        self.fstreams = {} # name: fstream (where name matches fstream.name)

        self.match_with_dec: Callable[[str], Optional[FileCloseParser.Fstream]] = FileCloseParser.declaration_matcher()

    @dataclass
    class Fstream:
        name: str
        opened: bool = False
        closed: bool = False

    # static methods that return a function that does some regex shih

    @staticmethod
    def declaration_matcher() -> Callable[[str], Optional["FileCloseParser.Fstream"]]:
        """
        Returns a function that takes in a `str` and returns a `Fstream` if the inputted 
        string contains a fstream declaration (or initialization).

        * Compatible with std::fstream, std::ifstream, std::ofstream, with or without `std::` pre-pending it.  
        * Compatible with raw declarations (`ifstream infile`), initializations (`ifstream infile("file.txt")`),
        or bracket initializations (`ifstream infile{"data.txt"}`).  
        * Compatible with `const`, `static`, and `extern` declarations.
        """
        pattern = re.compile(
            r"""
            ^\s*
            (?:(?:const|static|extern|mutable|register)\s+)*
            (?:std::)?
            (?:f|if|of)stream
            \s+
            (?P<name>[A-Za-z_]\w*)
            \s*
            (?:
                ;                                   # declaration only
                |
                (?P<init>\([^;]*\)|\{[^;]*\})\s*;  # initialized/opened
            )
            """,
            re.VERBOSE,
        )

        def matcher(line: str) -> Optional[FileCloseParser.Fstream]:
            match = pattern.match(line)
            if not match:
                return None

            return FileCloseParser.Fstream(
                name=match.group("name"),
                opened=match.group("init") is not None,
            )

        return matcher

    @staticmethod
    def open_matcher() -> Callable[[str], Optional["FileCloseParser.Fstream"]]:
        return lambda x: None

    @staticmethod
    def close_matcher() -> Callable[[str], Optional["FileCloseParser.Fstream"]]:
        return lambda x: None

    # the actual parsing & checking stuff for fstream closing

    def walk_through_file(self) -> None:
        for line in self.source_code:
            self.process_line(line.rstrip())

    def process_line(self, line:str) -> None:
        pass


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