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

def check_parser(file):
    parser = FileCloseParser(file=file)
    parser.walk_through_file()
    for fstream in parser.fstreams:
        print(fstream)

if __name__ == "__main__":
    data = sys.stdin.read() # capture stdin so I can reuse the data in its buffer
    buf1 = StringIO(data)
    buf2 = StringIO(data)
    check_matcher(buf1)
    print()
    check_parser(buf2)