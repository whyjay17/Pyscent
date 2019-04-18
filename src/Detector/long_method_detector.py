import sys
import os

sys.path.insert(0, 'CodeSmellHandlers/HandleLongMethodSmell')
import long_method as lm

def detect_long_method(directory):
    path, dirs, files = next(os.walk(directory))
    output = lm.output_long_methods(directory)
    # print (output.stdout)
    return [output.decode('utf-8') for output in output.splitlines() if len(output) > 3]

output_list = detect_long_method("../../code-dump/smaller-test")