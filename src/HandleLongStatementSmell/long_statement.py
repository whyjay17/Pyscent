import ast
import astor
import os


def detect_from_code_dump(directory,limit,type):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            long_stmt = detect_long_lanmbda_function(directory+"/"+filename, limit,type)
            if len(long_stmt)>3:
                print("========================")
                print(filename)
                print(long_stmt)
                print("========================")



def detect_long_lanmbda_function(file_path,limit,type):
    with open(file_path) as f:
        data = f.read()
        tree = ast.parse(data)
        return get_long_lambda_source(tree,limit,type)


def get_long_lambda_source(tree,limit,type):
    ret_arr = []
    for node in ast.walk(tree):
        if isinstance(node,type):
            lambda_str = astor.to_source(node)
            if len(lambda_str)>limit:
                ret_arr.append(lambda_str)
    return ret_arr


detect_from_code_dump("/Users/jaewookim/PycharmProjects/cs527_project/code-dump/flask-master",25,ast.Lambda)
detect_from_code_dump("/Users/jaewookim/PycharmProjects/cs527_project/code-dump/keras-master",25,ast.ListComp)

