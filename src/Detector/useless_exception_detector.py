import os
from .CodeSmellHandlers.HandleExceptionSmell.useless_exception import detect_useless_exception_per_file

def detect_useless_exception(directory):
    output_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            long_stmts = detect_useless_exception_per_file(directory + "/" + filename)
            output_list.append((filename,long_stmts))
    dir_name = directory.split('/')[-1]
    log_count = generate_log(dir_name, output_list)
    
    return ([line for line in output_list if line[1]], log_count)


def generate_log(dir_name, output_list):
    log_count = 0
    log = open(os.path.join("output", "logs", "useless_exception_logs.txt"), "w")
    for file in output_list:
        filename = file[0]
        smelly_lineno_list = file[1]
        if smelly_lineno_list:
            for lineno in smelly_lineno_list:
                log.write('FILENAME: {}, LINE: {} ({})\n'.format(filename, str(lineno[0]), lineno[1]))
                log_count += 1
    log.close()
    return log_count


# test run

# out = detect_useless_exception('../../code-dump/scikit-learn-master')