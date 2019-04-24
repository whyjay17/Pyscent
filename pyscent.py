
import sys
from subprocess import run, PIPE
import shlex
from src import detector

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == "__main__":
    # main()
    print(sys.argv)
    #detector.detect_main("./code-dump/"+sys.argv[1])

#if len(sys.argv) != 2:
#    print ("target directory not specified")
#cmd = "python3 tools/py_file_extractor ./sourcecode/"+sys.argv[1]
#result = run(shlex.split(cmd), stdout=PIPE)

#detect_main("./code-dump/"+sys.argv[1])



