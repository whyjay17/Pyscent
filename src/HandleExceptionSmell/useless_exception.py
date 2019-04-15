# Sources
## 1) https://lignos.org/py_antipatterns/
## 2) https://legacy.python.org/dev/peps/pep-0008/

import ast
import astor
from pprint import pprint


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
    
    with open(file_path) as f:
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
                                print('Line {}: Too general exception.'.format(handler.lineno))
                                smelly_lines.append(handler.lineno)
                                continue
                            if len(handler.body) == 1 and isinstance(handler.body[0], ast.Pass):
                                print('Line {}: Empty exception detected.'.format(handler.lineno))
                                smelly_lines.append(handler.lineno)
            # when the try/exception is in a function
            else:
                if isinstance(instance, ast.Try):
                    try_obj = instance
                    for handler in try_obj.handlers:
                        if handler.type is None or handler.type == 'Exception':
                            print('Line {}: Too general exception.'.format(handler.lineno))
                            smelly_lines.append(handler.lineno)
                            continue
                        if len(handler.body) == 1 and isinstance(handler.body[0], ast.Pass):
                            print('Line {}: Empty exception detected.'.format(handler.lineno))
                            smelly_lines.append(handler.lineno)

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
