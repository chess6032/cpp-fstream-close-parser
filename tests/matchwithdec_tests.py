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
    found = []
    SHOULD_HAVE_FOUND = [
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
        'u_multi_stmt1', 
        'u_multi_stmt2',
        'u_multi_dec1', 
        'u_multi_dec2',
    ]

    parser = FileCloseParser(file=file)
    parser.walk_through_file()

    for fstream in parser.fstreams.values():
        name = fstream.name
        found.append(fstream.name)

        print(name)
        assert name in SHOULD_HAVE_FOUND, f"FAIL: FALSE POSITIVE: {name}"

        assert not fstream.closed, f"FAIL: {name} marked as closed for some reason?"

        if name[0] == 'u':
            assert not fstream.opened, f"FAIL: {name} incorrectly marked as opened"
        elif name[0] == 'o':
            assert fstream.opened, f"FAIL: {name} incorrectly marked as UN-opened"
        else:
            raise RuntimeError(f"FAIL: incorrect match")

    print()

    for required in SHOULD_HAVE_FOUND:
        try:
            assert required in found, f"FAIL: FALSE NEGATIVE: {required}"
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    with sys.stdin as file:
        test_parser(file)