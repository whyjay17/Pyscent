import ast
from .CodeSmellHandlers.HandleLongStatementSmell.long_statement import output_long_statements

def detect_long_lambda(directory, limit):
    num_long_statements = 0
    output = output_long_statements(directory,limit,ast.Lambda)
    # print (output)
    for file_stmt_tuple in output[0]:
        num_long_statements += len(file_stmt_tuple[1])
    return (num_long_statements,output[1])


# detect_long_lambda("../../code-dump/flask-master", 25)