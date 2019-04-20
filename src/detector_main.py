import ast
import os
import fpdf
from Detector.class_coupling_detector import detect_class_cohesion
from Detector.cyclomatic_complexity_detector import detect_cyclomatic_complexity
from Detector.long_lambda_detector import detect_long_lambda
from Detector.long_list_comp_detector import detect_long_list_comp
from Detector.pylint_output_detector import detect_pylint_output
from Detector.shotgun_surgery_detector import detect_shotgun_surgery

def detect_main(directory):
    # Get stats for files in directory
    stats_dict = get_stats(directory)
    
    # Setup PDF
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    
    dirname = directory.split('/')[-1]
    
    # Print Title
    pdf.set_font("times", style='b', size=24)
    header_text = 'Code Smell Summary: {}'.format(dirname)
    write_pdf_line(pdf, header_text, 20)
    
    pdf.set_font("Arial", size=12)
    
    # Print Pylint Output
    header_text = "Long Methods"
    write_pdf_line(pdf, header_text, 10)
    long_method, long_params, long_branches, many_attrbs, many_methods = \
        detect_pylint_output(directory)
    pdf.set_font("times", size=12)
    pylint_text = "   - Number of Long Methods / Total number of Methods: {} / {}".format(str(long_method[0]), str(stats_dict["methods"]))
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "   - Longest Method:"
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * File Name: {}".format(long_method[1]['filename'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Line Number: {}".format(long_method[1]['lineno'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Number of Statements: {}".format(long_method[1]['metric'])
    write_pdf_line(pdf, pylint_text, 10)
    
    header_text = "Long Parameter"
    write_pdf_line(pdf, header_text, 10)
    pdf.set_font("times", size=12)
    pylint_text = "   - Number of Methods with Long Parameter / Total number of Methods: {} / {}".format(str(long_params[0]), str(stats_dict["methods"]))
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "   - Method with Longest Parameter:"
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * File Name: {}".format(long_params[1]['filename'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Line Number: {}".format(long_params[1]['lineno'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Number of Parameters: {}".format(long_params[1]['metric'])
    write_pdf_line(pdf, pylint_text, 10)
    
    header_text = "Long Branches"
    write_pdf_line(pdf, header_text, 10)
    pdf.set_font("times", size=12)
    pylint_text = "   - Number of Long Branches: {}".format(str(long_branches[0]))
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "   - Longest Branch:"
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * File Name: {}".format(long_branches[1]['filename'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Line Number: {}".format(long_branches[1]['lineno'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Number of Branches: {}".format(long_branches[1]['metric'])
    write_pdf_line(pdf, pylint_text, 10)
    
    header_text = "Too Many Attributes in Class"
    write_pdf_line(pdf, header_text, 10)
    pdf.set_font("times", size=12)
    pylint_text = "   - Number of Classes with Many Attributes: {}/{}".format(str(many_attrbs[0]), str(stats_dict["classes"]))
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "   - Class with most Attributes:"
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * File Name: {}".format(many_attrbs[1]['filename'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Line Number: {}".format(many_attrbs[1]['lineno'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Number of Attributes in Class: {}".format(many_attrbs[1]['metric'])
    write_pdf_line(pdf, pylint_text, 10)
       
    header_text = "Too Many Methods in Class"
    write_pdf_line(pdf, header_text, 10)
    pdf.set_font("times", size=12)
    pylint_text = "   - Number of Classes with Many Methods: {}/{}".format(str(many_methods[0]), str(stats_dict["classes"]))
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "   - Class with most methods:"
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * File Name: {}".format(many_methods[1]['filename'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Line Number: {}".format(many_methods[1]['lineno'])
    write_pdf_line(pdf, pylint_text, 10)
    pylint_text = "              * Number of Methods in Class: {}".format(many_methods[1]['metric'])
    write_pdf_line(pdf, pylint_text, 10)
    
    # Print useless try...except 
       
    header_text = "Too Many Methods in Class"
    write_pdf_line(pdf, header_text, 10)
    pdf.set_font("times", size=12)
    ##
    
    # Print Shotgun Surgery
    
    
    # Print Cohesion Output
    header_text = "Class Cohesion"
    write_pdf_line(pdf, header_text, 10)
    cohesion_output = detect_class_cohesion(directory, 30)
    cohesion_text = "   - Classes with Low Cohesion/Total number of Classe: {}/{}".format(str(cohesion_output), str(stats_dict["classes"]))
    write_pdf_line(pdf, cohesion_text, 5)
    # Print Code Complexity
    header_text = "Code Complexity"
    write_pdf_line(pdf, header_text, 10)
    cc_output = detect_cyclomatic_complexity(directory)
    cc_text = "   - Blocks with Cyclomatic Complexity Rank Lower than 'C' / Total Number of Code Blocks: {}/{}".format(str(cc_output), str(stats_dict["codeblocks"]))
    write_pdf_line(pdf, cc_text,5)
    # Print Long Lambda
    header_text = "Long Lambda"
    write_pdf_line(pdf, header_text, 10)
    long_lambda_output = detect_long_lambda(directory,30)
    long_lambda_text = "   - Number of Long Lambda Functions / Number of Lambda Functions: {}/{}".format(str(long_lambda_output[0]), str(stats_dict["lambdas"]))
    write_pdf_line(pdf, long_lambda_text,5)
    write_pdf_line(pdf, str(long_lambda_output[1]),5)
    # Print Long List Comprehension
    header_text = "Long List Comprehension"
    write_pdf_line(pdf, header_text, 10)
    long_list_comp_output = detect_long_list_comp(directory,30)
    long_list_comp_text = "   - Number of Long List Comprehension / Number of List Comprehensions: {}/{}".format(str(long_list_comp_output[0]), str(stats_dict["listcomps"]))
    write_pdf_line(pdf, long_list_comp_text, 5)
    write_pdf_line(pdf, str(long_list_comp_output[1]),5)
    # Output stream to PDF
    pdf.output("./{}_review.pdf".format(dirname))

def write_pdf_line(pdf, text, text_height):
    pdf.write(text_height,text)
    pdf.ln()


def get_stats(directory):
    total_num_method = 0
    total_num_class = 0
    total_num_lambda = 0
    total_num_try_catch = 0
    total_num_list_comp = 0
    total_num_code_blocks = 0
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            with open(directory + "/" + filename, encoding='UTF8') as f:
                data = f.read()
                tree = ast.parse(data)
                for node in ast.walk(tree):
                    if isinstance(node,ast.FunctionDef):
                        total_num_method+=1
                    if isinstance(node,ast.ClassDef):
                        total_num_class+=1
                    if isinstance(node,ast.Lambda):
                        total_num_lambda+=1
                    if isinstance(node,ast.Try):
                        total_num_try_catch += 1
                    if isinstance(node,ast.ListComp):
                        total_num_list_comp+=1
    total_num_code_blocks = total_num_method + total_num_class
    return {"methods":total_num_method,"classes":total_num_class,"lambdas":total_num_lambda,\
            "try":total_num_try_catch,"listcomps":total_num_list_comp,\
            "codeblocks":total_num_code_blocks}

detect_main("../code-dump/flask-master")


