import sys
import os

sys.path.insert(0, 'CodeSmellHandlers/HandleLongMethodSmell')
import long_method as lm

def detect_long_method(directory):
    path, dirs, files = next(os.walk(directory))
    output = lm.output_long_methods(directory)
    # print (output.stdout)
    return str(output.stdout)
    
res = detect_long_method("../../code-dump/smaller-test")