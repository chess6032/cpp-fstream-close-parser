import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from filecloseparser import FileCloseParser

if __name__ == "__main__":
    match_with_dec = FileCloseParser.declaration_matcher()
    with open(sys.argv[1]) as f:
        for line in f:
            if match_with_dec(line):
                print(line)