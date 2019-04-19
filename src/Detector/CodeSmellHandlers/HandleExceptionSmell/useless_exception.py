# Sources
## 1) https://lignos.org/py_antipatterns/
## 2) https://legacy.python.org/dev/peps/pep-0008/

import ast
import astor
from pprint import pprint
import os

def output_useless_exception(directory):
    output_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            long_stmts = detect_useless_exception(directory + "/" + filename)
            output_list.append((filename,long_stmts))
    dir_name = directory.split('/')[-1]
    generate_log(dir_name, output_list)
    
    return output_list


def generate_log(dir_name, output_list):
    log = open(r"\Users\YJ\Desktop\cs527_project\src\logs\{}_useless_exception_logs".format(dir_name), "w")
    for file in output_list:
        print(file)
        filename = file[0]
        smelly_lineno_list = file[1]
        if smelly_lineno_list:
            for lineno in smelly_lineno_list:
                log.write('filename: {}, smelly_lines: {} ({})\n'.format(filename, str(lineno[0]), lineno[1]))

def detect_useless_exception(file_path):
    """ 
    Detect Useless Exception: a try..except statement that does little
        Two types of useless exceptions:
            1) has only one except clause and catches a too general exception like Exception and Standard Error
            2) all exception clauses in the statement are empty
    
    Parameters: 
        file_path (string): path of the source code file to be detected
    
    Return:
        smelly_lines (list[int]): list of lines that are smelly
    
    """
    
    smelly_lines = []
    
    with open(file_path, "rt", encoding='UTF8') as f:
        data = f.read()
        module = ast.parse(data)
        for instance in module.body:
            # when the try/exception is in a function
            if isinstance(instance, ast.FunctionDef):
                # iterate through elements in the function
                for obj in instance.body:
                    if isinstance(obj, ast.Try):
                        try_obj = obj
                        for handler in try_obj.handlers:
                            if handler.type is None or handler.type == 'Exception':
                                smelly_lines.append((handler.lineno, 'Too general exception'))
                                continue
                            if len(handler.body) == 1 and isinstance(handler.body[0], ast.Pass):
                                smelly_lines.append((handler.lineno, 'Empty exception detected'))
            # when the try/exception is in a function
            else:
                if isinstance(instance, ast.Try):
                    try_obj = instance
                    for handler in try_obj.handlers:
                        if handler.type is None or handler.type == 'Exception':
                            smelly_lines.append((handler.lineno, 'Too general exception'))
                            continue
                        if len(handler.body) == 1 and isinstance(handler.body[0], ast.Pass):
                            smelly_lines.append((handler.lineno, 'Empty exception detected'))

    return smelly_lines
    

def get_function_name(def_object):
    """
    Convert ast.FunctionDef to function name string
    
    Parameters: 
        def_object (ast.FunctionDef): FunctionDef object in the Abstract String Tree
        
    Return:
        string: function name
        
    """
    func_str = astor.to_source(def_object)
    first_idx = func_str.index(' ')
    sec_idx = func_str.index('(')
    return func_str[first_idx + 1 : sec_idx]

# Test - Remove Later3
output_useless_exception("../../../../code-dump/scikit-learn-master")
