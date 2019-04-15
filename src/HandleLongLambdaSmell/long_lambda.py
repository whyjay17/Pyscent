

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

# print(get_long_lambda_source(test.test1))
# print(get_long_lambda_source(test.test2))
# print(get_long_lambda_source(test.test3))

with open('test.py') as f:
    data = f.read()
    module = ast.parse(data)
    function = module.body
    for obj in function:
        # print (obj.value)
        print(get_long_lambda_source(obj.value))
        # if isinstance(obj, ast.Lambda):
        #     try_block = obj
        #     print('number of excepts = {}'.format(len(try_block.handlers)))
        #     for handler in try_block.handlers:
        #         if handler.type is None or handler.type == 'Exception':
        #             print('Line {}: Too general exception.'.format(handler.lineno))
        #             continue
        #         if len(handler.body) == 1 and isinstance(handler.body[0], ast.Pass):
        #             print('Line {}: Empty exception detected.'.format(handler.lineno))

