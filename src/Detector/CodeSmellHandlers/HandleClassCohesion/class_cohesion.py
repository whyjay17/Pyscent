import shlex
from subprocess import run, PIPE
import os

def output_class_cohesion(directory):
    cmd = "cohesion --files " + get_file_list(directory) \
          # + "--below " + 100
    result = run(shlex.split(cmd), stdout=PIPE , cwd=directory)
    return result

def get_file_list(directory):
    file_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_list.append(filename + " ")
    return "".join(file_list)