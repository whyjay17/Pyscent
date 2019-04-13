# Useless Exception Handling: a try..except statement that does little
# Two types of useless exceptions:
## 1) has only one except clause and catches a too general exception like Exception and Standard Error
## 2) all exception clauses in the statement are empty

# Metrics Needed
## 1) Number of excepts
## 2) Number of General Exception
## 3) Number of empty excepts

# Sources
## 1) https://lignos.org/py_antipatterns/
## 2) https://legacy.python.org/dev/peps/pep-0008/

import ast
from pprint import pprint

with open('test.py') as f:
    data = f.read()
    module = ast.parse(data)
    function = module.body[0]
    print('number of try..except clauses = {}'.format(len([obj for obj in function.body if isinstance(obj, ast.Try)])))
    for obj in function.body:
        if isinstance(obj, ast.Try):
            try_block = obj
            print('number of excepts = {}'.format(len(try_block.handlers)))
            for handler in try_block.handlers:
                if handler.type is None or handler.type == 'Exception':
                    print('Line {}: Too general exception.'.format(handler.lineno))
                    continue
                if len(handler.body) == 1 and isinstance(handler.body[0], ast.Pass):
                    print('Line {}: Empty exception detected.'.format(handler.lineno))