import ast
import astor
import os


def output_long_statements(directory, limit, type):
    output_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            long_stmts = detect_long_statement(directory + "/" + filename, limit, type)
            if len(long_stmts):
                output_list.append((filename,long_stmts))
    worst_code = generate_log(output_list, type)
    return (output_list,worst_code)


def generate_log(output_list,type):
    worst = {}
    metric = 0
    if type == ast.Lambda:
        log = open(os.path.join("output", "logs", "long_lambda_logs.txt"), "w")
    else:
        log = open(os.path.join("output", "logs", "long_list_comp_logs.txt"), "w")
    for file in output_list:
        filename = file[0]
        stmt_lineno_list = file[1]
        for stmt_lineno in stmt_lineno_list:
            if metric < len(stmt_lineno[0]):
                worst = {"filename" : filename , "lineno" : stmt_lineno[1], "line length":len(stmt_lineno[0])}
                metric = len(stmt_lineno[0])
            log.write("filename: " + filename + " lineno: " + str(stmt_lineno[1]) + " metric: " + str(
                len(stmt_lineno[0])) + "\n")
    log.close()
    return worst



def detect_long_statement(file_path, limit, type):
    with open(file_path, encoding='UTF8') as f:
        data = f.read()
        tree = ast.parse(data)
        output = get_long_statement_source(tree, limit, type)
        return output


def get_long_statement_source(tree, limit, type):
    ret_arr = []
    for node in ast.walk(tree):
        if isinstance(node,type):
            statement_str = astor.to_source(node)[0:-1]
            if len(statement_str)>limit:
                ret_arr.append((statement_str,node.lineno))
    return ret_arr


# output_long_statements("../../../../code-dump/flask-master", 25, ast.Lambda)
# output_long_statements("../../../../code-dump/keras-master", 25, ast.ListComp)

