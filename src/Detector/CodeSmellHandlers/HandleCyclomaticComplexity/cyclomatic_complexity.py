import shlex
from subprocess import run, PIPE
import os

def output_cyclomatic_complexity(directory):
    cmd = "radon cc ./ --a -nc"
    result = run(shlex.split(cmd), stdout=PIPE , cwd=directory)
    return result
