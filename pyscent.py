
import sys
from subprocess import run, PIPE
import shlex
from src.detector_main import detect_main



if len(sys.argv) != 2:
    print ("target directory not specified")
cmd = "python3 tools/py_file_extractor ./sourcecode/"+sys.argv[1]
result = run(shlex.split(cmd), stdout=PIPE)

detect_main("./code-dump/"+sys.argv[1])



