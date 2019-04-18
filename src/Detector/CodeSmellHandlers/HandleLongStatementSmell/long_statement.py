import ast
import astor
import os


def output_long_statements(directory, limit, type):
    output_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            long_stmts = detect_long_statement(directory + "/" + filename, limit, type)
            output_list.append((filename,long_stmts))
            # print(filename)
            # print(long_stmts)
    return output_list




def detect_long_statement(file_path, limit, type):
    with open(file_path) as f:
        data = f.read()
        tree = ast.parse(data)
        return get_long_statement_source(tree, limit, type)


def get_long_statement_source(tree, limit, type):
    ret_arr = []
    for node in ast.walk(tree):
        if isinstance(node,type):
            statement_str = astor.to_source(node)[0:-1]
            if len(statement_str)>limit:
                ret_arr.append(statement_str)
    return ret_arr


output_long_statements("/Users/jaewookim/PycharmProjects/cs527_project/code-dump/flask-master", 25, ast.Lambda)
output_long_statements("/Users/jaewookim/PycharmProjects/cs527_project/code-dump/keras-master", 25, ast.ListComp)

