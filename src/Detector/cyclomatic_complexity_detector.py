from .CodeSmellHandlers.HandleCyclomaticComplexity.cyclomatic_complexity import output_cyclomatic_complexity

def detect_cyclomatic_complexity(directory):
    output = output_cyclomatic_complexity(directory)
    output_arr = output.stdout.splitlines()

    # print("cyclomatic",output_arr)
    # print(output.stdout.splitlines()[-3].split())
    number_of_blocks = output_arr[-2].split()[0] if output_arr else 0
    # print(number_of_blocks)
    # number_of_blocks = output_arr[-3].split()[0]
    # number_of_blocks = output_arr[-2].split()[0]

    return int(number_of_blocks)


# print("number of code blocks with cyclomatic complexity lower than C rank: " + str(detect_cyclomatic_complexity("../../code-dump/flask-master")))