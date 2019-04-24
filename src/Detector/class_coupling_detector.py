from .CodeSmellHandlers.HandleClassCohesion.class_cohesion import output_class_cohesion
import os


def detect_class_cohesion(directory, limit):
    path, dirs, files = next(os.walk(directory))
    output = output_class_cohesion(directory)
    total_num_targets = 0

    output_arr = str(output.stdout).split()
    for idx,word in enumerate(output_arr):
        if word == "Total:":
            target_percentage = float(output_arr[idx + 1].split("%")[0])
            if target_percentage<limit and target_percentage != 0.0:
                total_num_targets +=1
    # print("total number of classes with cohesion below " + str(limit) + " percent: " + str(total_num_targets) )
    return total_num_targets

# detect_class_cohesion("../../code-dump/flask-master", 50)