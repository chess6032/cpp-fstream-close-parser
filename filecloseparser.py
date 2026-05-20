import sys
from io import TextIOWrapper

class FstreamDeclaration:
    def __init__(self, name: str, loc):
        self.name = name
        self.loc = loc # TODO: what type for loc?

def identify_filestreams(file: TextIOWrapper) -> list[FstreamDeclaration]:
    return []

def find_close(file: TextIOWrapper, fstream: FstreamDeclaration):
    """Starting at `fstream.loc`, look for `<fstream.name>.close()` in `file`."""
    return None

def check_for_close(file: TextIOWrapper, fstreams: list[FstreamDeclaration]) -> list[bool]:
    results = []

    for fstream in fstreams:
        if find_close(file, fstream):
            results.append(True)
        else:
            results.append(False)

    return results

def closes_all_filestreams(file: TextIOWrapper) -> bool:
    fstreams = identify_filestreams(file)
    results = check_for_close(file, fstreams)
    return False in results

if __name__ == "__main__":
    result = None
    with open(sys.argv[1]) as f:
        result = closes_all_filestreams(f)

    if result:
        exit(0)
    else:
        exit(1)