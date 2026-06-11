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
        'u_cmt_test2',
        'u_indent0',
        'u_indent1',
        'u_indent2',
        'u_indent3',
        'u_indent4',
        'u_indent_many',
        'u_indent_t1',
        'u_indent_t4',
        'u_ifstatement1',
        'u_ifstatement2',
        'u_ifstatement3',
    ]:
        try:
            assert required in fstreams, f"FAIL: MATCH MISS: {required}"
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    with sys.stdin as file:
        test_parser(file)