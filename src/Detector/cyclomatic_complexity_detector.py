from HandleCyclomaticComplexity.cyclomatic_complexity import output_cyclomatic_complexity

def detect_cyclomatic_complexity(directory):
    output = output_cyclomatic_complexity(directory)
    output_arr = output.stdout.splitlines()
    number_of_blocks = output_arr[-3].split()[0]
    return int(number_of_blocks)


print("number of code blocks with cyclomatic complexity lower than C rank: " + str(detect_cyclomatic_complexity("../../code-dump/flask-master")))