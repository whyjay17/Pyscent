
import inspect
import test
import ast

def get_long_lambda_source(lambda_func):
    try:
        source_lines = inspect.getsource(lambda_func)
        print (source_lines)
    except IOError:
        return None

    if len(source_lines) > 10:
        return source_lines
    return None

print(get_long_lambda_source(test.test1))
print(get_long_lambda_source(test.test2))
print(get_long_lambda_source(test.test3))


def get_short_lambda_ast_node(lambda_func):
    source_text = get_long_lambda_source(lambda_func)
    if source_text:
        source_ast = ast.parse(source_text)
        return next((node for node in ast.walk(source_ast)
                     if isinstance(node, ast.Lambda)), None)

    if len(source_lines) > 1:
        return None
    return source_lines


from pprint import pprint

with open('test.py') as f:
    data = f.read()
    module = ast.parse(data)
    function = module.body[0]
    for obj in function.body:
        print(obj)

