
import sys
from subprocess import run, PIPE
import shlex
from src import detector
import os
from shutil import *
import fnmatch

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)

def file_extractor(proj_path):
    # if len(sys.argv) != 2:
    #     print("target directory not specified")
    # print('cwd',os.getcwd())
    matches = []
    path = os.path.join("code-dump", os.path.basename(proj_path))
    # path = "../code-dump" +"/"+os.path.basename(sys.argv[1])
    if not os.path.exists(path):
        os.makedirs(path)
    # dst = "../code-dump" +"/"+os.path.basename(sys.argv[1])
    dst = os.path.join("code-dump", os.path.basename(proj_path))

    for the_file in os.listdir(path):
        file_path = os.path.join(path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

    # print(sys.argv[1])

    for root, dirnames, filenames in os.walk(proj_path):
        for filename in fnmatch.filter(filenames, '*.py'):
            matches.append(os.path.join(root, filename))

    for idx,src in enumerate(matches):
        copy(src, dst)
        # print(dst+"/"+os.path.basename(src))
        os.rename(dst+"/"+os.path.basename(src), dst+"/"+str(idx)+os.path.basename(src))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("target directory not specified")
    
    file_extractor(sys.argv[1])
    # print(os.path.basename(sys.argv[1]))
    #extractor_path = os.path.join("tools", "py_file_extractor.py")
    ##cmd = "python {} {}".format(extractor_path, sys.argv[1])
    #print('cmd', cmd)
    #result = run(shlex.split(cmd), stdout=PIPE)
    #print('cmd2', cmd.split("/")[-1])
    # dump_path = os.path.join("code-dump", sys.argv[1])
    detector.detect_main("./code-dump/" + os.path.basename(sys.argv[1]))
    print('*****     Output Generated     *****')

#if len(sys.argv) != 2:
#    print ("target directory not specified")
#cmd = "python3 tools/py_file_extractor ./sourcecode/"+sys.argv[1]
#result = run(shlex.split(cmd), stdout=PIPE)

#detect_main("./code-dump/"+sys.argv[1])



