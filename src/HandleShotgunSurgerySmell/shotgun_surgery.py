# Shotgun Surgery: 
## A shotgun surgery can be when a change to a "Class A" causes several minor changes to other classes
## Shotgun surgery happens when you have to make many changes in your codebase to achieve seemingly simple tasks

# How to detect
## 1. Count the number of external function calls (not the member of the class) within a class.
## 2. If the number of external function calls is > n, it is a smell

import ast
import astor

def detect_shotgun_surgery(file_path):
    """ 
    Detect Shotgun Surgery: number of external function calls within a class
    
    Parameters: 
        file_path (string): path of the source code file to be detected
    
    Return:
        analysis (dict[string]: (string, bool)): ClassName: (number of external calls / total calls, isSmelly)
    
    """
    
    analysis = {}
    with open(file_path) as f:
        data = f.read()
        module = ast.parse(data)
        for instance in module.body:
            if isinstance(instance, ast.ClassDef):
                functions, external_count, total_count = [], 0, 0
                for classObj in instance.body:
                    if isinstance(classObj, ast.FunctionDef):
                        functions.append(classObj.name)
                for classObj in ast.walk(instance):
                    if isinstance(classObj, ast.Call):
                        if astor.to_source(classObj).split('(')[0] not in functions and \
                            'error' not in astor.to_source(classObj).split('(')[0].lower():
                            external_count += 1
                        total_count += 1
                analysis[instance.name] = ('{}/{} (external calls / total)'.format(external_count, total_count), \
                        True if external_count > 0 else False)
                        # TODO: decide metric n
    
    return analysis

