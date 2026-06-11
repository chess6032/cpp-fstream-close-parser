import sys
import os
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from filecloseparser import FileCloseParser

def check_matcher(file):
    match_with_dec = FileCloseParser.declaration_matcher()
    for line in file:
        if match_with_dec(line):
            print(line)

def test_parser(file):
    parser = FileCloseParser(file=file)
    parser.walk_through_file()
    for fstream in parser.fstreams:
        name = fstream.name
        print(name)
        if name[0] == 'u':
            assert not fstream.opened
        elif name[0] == 'o':
            assert fstream.opened
        else:
            raise RuntimeError(f"incorrect match")


if __name__ == "__main__":
    with sys.stdin as file:
        test_parser(file)