import sys
from io import TextIOWrapper



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {str(sys.argv[0])} filepath")
        sys.exit(2)

    result = None
    with open(sys.argv[1]) as f:
        pass # TODO

    if result:
        sys.exit(0)
    else:
        sys.exit(1)