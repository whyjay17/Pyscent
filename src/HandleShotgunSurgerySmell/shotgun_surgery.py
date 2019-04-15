# Shotgun Surgery: 
## A shotgun surgery can be when a change to a "Class A" causes several minor changes to other classes
## Shotgun surgery happens when you have to make many changes in your codebase to achieve seemingly simple tasks

# How to detect
## 1. Count the number of external function calls (not the member of the class) within a class.
## 2. If the number of external function calls is > n, it is a smell

import ast
import astor
from pprint import pprint

def detect_shotgun_surgery(file_path):
    """ 
    Detect Shotgun Surgery: number of external function calls within a class
    
    Parameters: 
        file_path (string): path of the source code file to be detected
    
    Return:
        smelly_lines (list[int]): list of lines that are smelly
    
    """
    