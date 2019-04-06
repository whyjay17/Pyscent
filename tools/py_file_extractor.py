import fnmatch
import os
import sys

from shutil import *


if len(sys.argv) != 2:
    print "target directory not specified"

matches = []
path = "../code-dump" +"/"+os.path.basename(sys.argv[1])
if not os.path.exists(path):
    os.makedirs(path)
dst = "../code-dump" +"/"+os.path.basename(sys.argv[1])

for the_file in os.listdir(path):
    file_path = os.path.join(path, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

print sys.argv[1]

for root, dirnames, filenames in os.walk(sys.argv[1]):
    for filename in fnmatch.filter(filenames, '*.py'):
        matches.append(os.path.join(root, filename))

for idx,src in enumerate(matches):
    copy(src, dst)
    print dst+"/"+os.path.basename(src)
    os.rename(dst+"/"+os.path.basename(src), dst+"/"+str(idx)+os.path.basename(src))