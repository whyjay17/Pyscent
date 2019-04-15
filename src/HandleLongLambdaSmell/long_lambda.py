import ast
import astor
import os


def detect_from_code_dump(directory,limit):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            long_lambdas = detect_long_lanmbda_function(directory+"/"+filename, limit)
            if len(long_lambdas)>3:
                print("========================")
                print(filename)
                print(long_lambdas)
                print("========================")



def detect_long_lanmbda_function(file_path,limit):
    with open(file_path) as f:
        data = f.read()
        tree = ast.parse(data)
        return get_long_lambda_source(tree,limit)


def get_long_lambda_source(tree,limit):
    ret_arr = []
    for node in ast.walk(tree):
        if isinstance(node,ast.Lambda):
            lambda_str = astor.to_source(node)
            if len(lambda_str)>limit:
                ret_arr.append(lambda_str)
    return ret_arr


detect_from_code_dump("/Users/jaewookim/PycharmProjects/cs527_project/code-dump/flask-master",25)

