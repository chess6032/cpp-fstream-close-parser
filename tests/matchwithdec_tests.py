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
    fstreams = []

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
        fstreams.append(fstream.name)

    for required in [
        'uF1',
        'uF2',
        'uF3',
        'uF4',
        'oF1',
        'oF2',
        'oF3',
        'oF4',
        'oF5',
        'oF6',
        'oF7',
        'oF8',
        'u_cmt_test1',
        'u_cmt_test2'
    ]:
        assert required in fstreams


if __name__ == "__main__":
    with sys.stdin as file:
        test_parser(file)