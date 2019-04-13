"""
with open("test.py", "r") as f:
    content = f.readlines()
    for line in content:
        if "lambda" in line:
            print(line)

def get_short_lambda_source(lambda_func):
    try:
        source_lines, _ = inspect.getsource(lambda_func)
    except IOError:
        return None
    if len(source_lines) > 1:
        return None
    return source_lines
"""

import ast
from pprint import pprint

with open('test.py') as f:
    data = f.read()
    module = ast.parse(data)
    function = module.body[0]
    for obj in function.body:
        print(obj)