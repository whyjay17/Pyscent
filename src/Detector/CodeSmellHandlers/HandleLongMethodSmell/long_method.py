import shlex
from subprocess import run, PIPE
import os

def output_long_methods(directory):
    """ 
    return stdout of the pylint refactoring (R) command
    
    Parameters: 
        directory (string): path of the directory of source code files
    
    Return:
        result.stdout (byte): stdout of the pylint command
    
    """
    
    # just print refactoring messages
    cmd = "pylint --disable=E,W,C,F,I " + get_file_list(directory)
    result = run(shlex.split(cmd), stdout=PIPE , cwd=directory)

    return result.stdout

def get_file_list(directory):
    file_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_list.append(filename + " ")
    return "".join(file_list)