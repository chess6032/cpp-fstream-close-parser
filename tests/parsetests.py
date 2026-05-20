import sys
import subprocess
import os

def test_on_file(filepath: str):
    if "bad" not in filepath and "good" not in filepath:
        raise RuntimeError(f"{filepath} does not have 'bad' or 'good' in its name")

    result = subprocess.run(["python", "filecloseparser.py", filepath]).returncode

    if result == 0:
        return True if "good" in filepath else False
    elif result == 1:
        return True if "bad" in filepath else False
    if result == 0 or result == 1:
        return result
    else:
        raise RuntimeError(f"Bad exit code: {result}")

def test_directory(dirpath: str):
    filepaths: list[str] = []
    with os.scandir(dirpath) as entries:
        for entry in entries:
            if entry.is_file():
                filepaths.append(f"{dirpath}/{entry.name}")
    
    for filepath in filepaths:
        print(f'{filepath}')
        try:
            if not test_on_file(filepath):
                print("\tFailed :(")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    test_directory(sys.argv[1])