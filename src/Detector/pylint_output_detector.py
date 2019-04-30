import sys
import os
import collections
import re
# import CodeSmellHandlers.HandleLongMethodSmell.long_method as lm
from .CodeSmellHandlers.HandleLongMethodSmell.long_method import output_long_methods
def detect_pylint_output(directory):
    
    output_list = detect_pylint_output_helper(directory)
    analyzed = analyze_result(output_list)
    dirname = directory.split('/')[-1]
    generate_log(dirname, analyzed)

    # type: (total number, largest metric)
    na_tuple = (0, {'filename': 'N/A', 'lineno': 'N/A', 'metric': 'N/A'})
    num_long_methods = (len(analyzed['long_method']), analyzed['long_method'][0]) if len(analyzed['long_method']) > 0 else na_tuple
    num_long_params = (len(analyzed['long_parameter']), analyzed['long_parameter'][0]) if len(analyzed['long_parameter']) > 0 else na_tuple
    num_long_branches = (len(analyzed['too_many_branches']),analyzed['too_many_branches'][0]) if len(analyzed['too_many_branches']) > 0 else na_tuple
    num_many_attrb = (len(analyzed['too_many_attributes']), analyzed['too_many_attributes'][0]) if len(analyzed['too_many_attributes']) > 0 else na_tuple
    num_many_methods = (len(analyzed['too_many_methods']), analyzed['too_many_methods'][0]) if len(analyzed['too_many_methods']) > 0 else na_tuple
    return num_long_methods, num_long_params, num_long_branches, \
            num_many_attrb, num_many_methods
    
    
def detect_pylint_output_helper(directory):
    """ 
    Categorize smells based on their types and put filename, lineno, and metric info
    
    Parameters: 
        directory (string): path of the directory of source code files
    
    Return:
        output_lines (list[str]): list of pylint stdout
    
    """
    path, dirs, files = next(os.walk(directory))
    output = output_long_methods(directory).decode('utf-8')
    split_lines = output.splitlines()
    output_lines = [output for output in split_lines if len(output) > 3 and\
                    re.search("(R0915|R0913|R0912|R0904|R0902)", output) is not None]
    return output_lines


def analyze_result(smell_list):
    """ 
    Categorize smells based on their types and put filename, lineno, and metric info
    
    Parameters: 
        smell_list (list): list of lines parsed from the pylint stdout
    
    Return:
        smell_info (dict[list[dict]]): smell information categorized by smell_type
    
    """
    
    analyzed = collections.defaultdict(list)
    for elem in smell_list:
        elem = smell_to_obj(elem)
        analyzed[elem['smell_type']].append({'filename': elem['filename'], \
                'lineno': elem['lineno'], 'metric': elem['metric']})
    sorted_analyzed = collections.defaultdict(list)
    for smell in ['long_method', 'long_parameter', 'too_many_branches', 'too_many_methods', 'too_many_attributes']:
        sorted_analyzed[smell] = sorted(analyzed[smell], key = lambda x: x['metric'], reverse = True)

    return sorted_analyzed


def smell_to_obj(smell):
    """ 
    Convert a smell statement into an object
    
    Parameters: 
        smell (string): line parsed from the pylint stdout
    
    Return:
        obj (dict): obj that contains filename, line, smell type, and metric
    
    """
    
    smell_name = {'R0915': 'long_method', 'R0913': 'long_parameter', \
                  'R0912': 'too_many_branches', 'R0904': 'too_many_methods', \
                  'R0902': 'too_many_attributes'}
    
    tokens = [tok.lstrip() for tok in smell.split(':')]
    filename, lineno = tokens[0], int(tokens[1])
    smell_type = tokens[3]
    first, sec = tokens[4].find('('), tokens[4].find('/')
    metric = int(tokens[4][first + 1 : sec])
    obj = {'filename': filename, 'lineno': lineno, 'smell_type': smell_name[smell_type], \
           'metric': metric}
        
    return obj

def generate_log(dirname, log_object):
    for smell in log_object:  
        if not os.path.exists(os.path.join("output", "logs")):
            os.makedirs(os.path.join("output", "logs"))
        log = open(os.path.join("output", "logs", "{}_logs.txt").format(smell), "w")
        for elem in log_object[smell]:
            log.write('filename: {}, smelly_lines: {}, metric: {}\n'.format(elem['filename'], str(elem['lineno']), str(elem['metric'])))
    log.close()
# TEST Runs: remove later
            
#obj, num_long_methods, num_long_params, num_long_branches, num_many_attrb, num_many_methods = \
#detect_pylint_output("../../code-dump/flask-master")

    