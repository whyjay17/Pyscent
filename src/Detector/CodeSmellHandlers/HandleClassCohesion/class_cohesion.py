import shlex
from subprocess import run, PIPE
import os

def output_class_cohesion(directory):
    print(directory)
    cmd = "cohesion --files " + get_file_list(directory) \
          # + "--below " + 100
    output = run(shlex.split(cmd), stdout=PIPE , cwd=directory)
    generate_log(output.stdout.decode("utf-8").splitlines())
    return output


def generate_log(output):
    print (output[1])
    # log = open("../../logs/class_cohesion_logs", "w")
    # for file in output_list:
    #     filename = file[0]
    #     stmt_lineno_list = file[1]
    #     for stmt_lineno in stmt_lineno_list:
    #         log.write("filename: " + filename + " lineno: " + str(stmt_lineno[1]) + " metric: " + str(
    #             len(stmt_lineno[0])) + "\n")
def get_file_list(directory):
    file_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_list.append(filename + " ")
    return "".join(file_list)