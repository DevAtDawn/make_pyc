import py_compile
import sys
import pathlib
from pathlib import Path

def main():
    files = sys.argv
    for x in files:
        p = Path(x)
        out_file = str(p.with_name(p.stem).with_suffix('.pyc'))
        py_compile.compile(x, out_file)
        
if __name__ == "__main__":
    main()
