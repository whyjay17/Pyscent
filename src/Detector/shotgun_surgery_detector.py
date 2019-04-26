import os
import collections

from .CodeSmellHandlers.HandleShotgunSurgerySmell.shotgun_surgery import detect_shotgun_surgery_per_file


def detect_shotgun_surgery(directory):
    output_list = output_shotgun_surgery(directory)
    num_smelly_class, top = shotgun_output_formatter(output_list)

    return num_smelly_class, top


def shotgun_output_formatter(output_list):
    smelly_class = 0
    most_external_call = 0
    for key in output_list:
        smelly_class += len(output_list[key])

    top_class = ('N/A', 'N/A', 'N/A')

    for fileName in output_list:
        for className in output_list[fileName]:
            if most_external_call < len(output_list[fileName][className]) - 1:
                most_external_call = len(output_list[fileName][className])
                top_class = (fileName, className, most_external_call)

    return smelly_class, top_class


def output_shotgun_surgery(directory):
    output_list = collections.defaultdict(list)
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            ss = detect_shotgun_surgery_per_file(directory + "/" + filename)
            if len(ss) > 0:
                output_list[filename] = ss

    return output_list

# test run: remove later
# output = output_shotgun_surgery("../../code-dump/flask-master")
# ssout, top = detect_shotgun_surgery("../../code-dump/flask-master")