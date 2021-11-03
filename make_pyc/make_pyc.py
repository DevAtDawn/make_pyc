import py_compile
import sys
def main():
    files = sys.argv
    for x in files:
        py_compile.compile(x)
        
if __name__ == "__main__":
    main()
