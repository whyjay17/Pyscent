import inspect
import test

# with open("test.py", "r") as f:
#     content = f.readlines()
#     for line in content:
#         if "lambda" in line:
#             print(line)

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