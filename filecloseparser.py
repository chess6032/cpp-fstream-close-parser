import sys
import re
from io import TextIOWrapper

# Matches: [std::]ifstream/ofstream <name>
FSTREAM_PATTERN = re.compile(
    r'\b(?:std::)?(?:i|o)fstream\s+([a-zA-Z_][a-zA-Z0-9_]*)'
)

class FstreamDeclaration:
    def __init__(self, name: str, loc: int):
        """`name` is the fstream's variable name.
        `loc` is the 0-based line index of its declaration."""
        self.name = name
        self.loc = loc  # int: 0-based line index

def identify_filestreams(file: TextIOWrapper) -> list[FstreamDeclaration]:
    """Search `file` for filestream declarations."""
    file.seek(0)
    declarations = []
    for lineno, line in enumerate(file):
        # Skip comments and string literals (basic strip of // comments)
        code = line.split("//")[0]
        for match in FSTREAM_PATTERN.finditer(code):
            name = match.group(1)
            declarations.append(FstreamDeclaration(name, lineno))
    return declarations

def find_close(file: TextIOWrapper, fstream: FstreamDeclaration) -> int | None:
    """Starting at `fstream.loc`, look for `<fstream.name>.close()` in `file`.
    If found, returns the 0-based line index of the `.close()` call."""
    # Build a pattern like: foo.close()  (whitespace-tolerant)
    close_pattern = re.compile(
        r'\b' + re.escape(fstream.name) + r'\s*\.\s*close\s*\(\s*\)'
    )
    file.seek(0)
    for lineno, line in enumerate(file):
        if lineno < fstream.loc:
            continue
        code = line.split("//")[0]
        if close_pattern.search(code):
            return lineno
    return None

def check_for_closes(file: TextIOWrapper, fstreams: list[FstreamDeclaration]) -> list[bool]:
    """Searches `file` for closing statements for all fstreams in `list`.
    Returns a list of bools, such that the `i`th item is `True` if `fstreams[i]`
    was closed."""
    results = []
    for fstream in fstreams:
        if find_close(file, fstream) is not None:
            results.append(True)
        else:
            results.append(False)
    return results

def closes_all_filestreams(file: TextIOWrapper) -> bool:
    """Returns `True` if all filestreams in `file` were closed."""
    fstreams = identify_filestreams(file)
    if not fstreams:
        return True  # No filestreams => nothing to close
    results = check_for_closes(file, fstreams)
    return False not in results  # Fixed: was `False in results`

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: checker.py <file.cpp>")
        sys.exit(2)

    result = None
    with open(sys.argv[1]) as f:
        result = closes_all_filestreams(f)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)