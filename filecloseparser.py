import sys
from io import TextIOWrapper
import re
from typing import Callable

class FileCloseParser:
    def __init__(self, file: TextIOWrapper):
        self.file = file
        self.fstreams = []

    class Fstream:
        def __init__(self, name:str):
            self.name = name

    # static methods that return a function that does some regex shih

    @staticmethod
    def match_with_declaration(line: str) -> Callable:
        return lambda: None

    @staticmethod
    def match_with_open(line: str) -> Callable:
        return lambda: None

    @staticmethod
    def match_with_close(line: str) -> Callable:
        return lambda: None

    # the actual parsing & checking stuff for fstream closing

    def walk_through_file(self) -> None:
        for line in self.file:
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