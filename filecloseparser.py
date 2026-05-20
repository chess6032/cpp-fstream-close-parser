import sys
from io import TextIOWrapper

class FstreamDeclaration:
    def __init__(self, name: str, loc):
        """`name` is the variable fstream's variable name.
        `loc` is the location of its declaration in the file it's in."""
        self.name = name
        self.loc = loc # TODO: what type for loc?

def identify_filestreams(file: TextIOWrapper) -> list[FstreamDeclaration]:
    """Search `file` for filestream delcarations."""
    return []

def find_close(file: TextIOWrapper, fstream: FstreamDeclaration):
    """Starting at `fstream.loc`, look for `<fstream.name>.close()` in `file`.
    If found, returns location of `.close()` in `file`."""
    return None

def check_for_closes(file: TextIOWrapper, fstreams: list[FstreamDeclaration]) -> list[bool]:
    """Searches `file` for closing statements for all fstreams in `list`.
    Returns a list of bools, such that the `i`th item is `True` if the `fstreams[i]`
    was closed."""
    results = []

    for fstream in fstreams:
        if find_close(file, fstream):
            results.append(True)
        else:
            results.append(False)

    return results

def closes_all_filestreams(file: TextIOWrapper) -> bool:
    """Returns `True` if all filestreams in `file` were closed."""
    fstreams = identify_filestreams(file)
    results = check_for_closes(file, fstreams)
    return False in results

if __name__ == "__main__":
    result = None
    with open(sys.argv[1]) as f:
        result = closes_all_filestreams(f)

    if result:
        exit(0)
    else:
        exit(1)