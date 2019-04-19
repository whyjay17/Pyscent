import ast
import os
import fpdf
from Detector.class_coupling_detector import detect_class_cohesion
from Detector.cyclomatic_complexity_detector import detect_cyclomatic_complexity
from Detector.long_lambda_detector import detect_long_lambda
from Detector.long_list_comp_detector import detect_long_list_comp
def detect_main(directory):
# Get stats for files in directory
    stats_dict = get_stats(directory)
# Setup PDF
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
# Print Cohesion Output
    header_text = "Class Cohesion"
    write_pdf_line(pdf, header_text, 10)
    cohesion_output = detect_class_cohesion(directory, 30)
    cohesion_text = "classes with low cohesion/total number of classes: " + str(cohesion_output) +"/" + str(stats_dict["classes"])
    write_pdf_line(pdf, cohesion_text,5)
# Print Code Complexity
    header_text = "Code Complexity"
    write_pdf_line(pdf, header_text, 10)
    cc_output = detect_cyclomatic_complexity(directory)
    cc_text = "blocks with cyclomatic complexity rank lower than 'C'/total number of code blocks: " + str(cc_output) +"/" + str(stats_dict["codeblocks"])
    write_pdf_line(pdf, cc_text,5)
# Print Long Lambda
    header_text = "Long Lambda"
    write_pdf_line(pdf, header_text, 10)
    long_lambda_output = detect_long_lambda(directory,30)
    long_lambda_text = "number of long lambda functions/number of lambda functions: " + str(long_lambda_output[0])+ "/" + str(stats_dict["lambdas"])
    write_pdf_line(pdf, long_lambda_text,5)
    write_pdf_line(pdf, str(long_lambda_output[1]),5)
# Print Long List Comprehension
    header_text = "Long List Comprehension"
    write_pdf_line(pdf, header_text, 10)
    long_list_comp_output = detect_long_list_comp(directory,30)
    long_list_comp_text = "number of long lambda functions/number of lambda functions: " + str(long_list_comp_output[0])+ "/" + str(stats_dict["listcomps"])
    write_pdf_line(pdf, long_list_comp_text, 5)
    write_pdf_line(pdf, str(long_list_comp_output[1]),5)
# Output stream to PDF
    pdf.output("./testings.pdf")

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
            with open(directory + "/" + filename) as f:
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


