# Shotgun Surgery:
## A shotgun surgery can be when a change to a "Class A" causes several minor changes to other classes
## Shotgun surgery happens when you have to make many changes in your codebase to achieve seemingly simple tasks

# How to detect
## 1. Count the number of external function calls (not the member of the class) within a class.
## 2. If the number of external function calls is > n, it is a smell

import ast
import astor
import collections


def detect_shotgun_surgery_per_file(file_path):
    """
    Detect Shotgun Surgery: number of external function calls within a class

    Parameters:
        file_path (string): path of the source code file to be detected

    Return:
        analysis (dict[string]: (string, bool)): ClassName: (number of external calls / total calls, isSmelly)

    """
    # TODO: exclude function calls from stdlib or pip-packages
    analysis = collections.defaultdict(list)
    with open(file_path, encoding='UTF8') as f:
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
                        if astor.to_source(classObj).split('(')[0].split('.')[-1] not in functions and \
                                astor.to_source(classObj).split('(')[0].split('.')[-1] not in dir(__builtins__):
                            external_count += 1
                            analysis[instance.name].append(classObj.lineno)
                        total_count += 1

                if external_count > 5:  # n = 5
                    analysis[instance.name].append('{}/{} (external calls / total)'.format(external_count, total_count))
                    # analysis[instance.name].append(True if external_count > 0 else False)
                # TODO: decide metric n

    return analysis

# ana = detect_shotgun_surgery_per_file('sample_file.py')