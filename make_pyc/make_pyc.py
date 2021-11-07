import py_compile
import sys
import pathlib
from pathlib import Path
cwd = Path.cwd()

def main():
    files = sys.argv
    for x in files[1:]:
        p = Path(x)
        out_file = str(p.with_name(p.stem).with_suffix('.pyc'))
        py_compile.compile(x, out_file)
#         py_compile.compile(x, cwd / out_file)

        
if __name__ == "__main__":
    main()
