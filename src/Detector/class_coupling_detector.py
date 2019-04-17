import class_cohesion as ch
import os


def detect_class_cohesion(directory, limit):
    path, dirs, files = next(os.walk(directory))
    output = ch.output_class_cohesion(directory, limit)
    print(str(output.stdout).split())
    print(float(str(output.stdout).split().count("Total:")))
    print("number of files with cohesion below " + str(limit) + "% : " + str(float(str(output.stdout).split().count("Total:")) / len(files)))
    # print (output.stdout)

detect_class_cohesion("../../code-dump/flask-master", 50)