import inspect
from test import TextImageGenerator

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