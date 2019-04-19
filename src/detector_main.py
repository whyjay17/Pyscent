import ast
import os
import fpdf

def detect_main(directory):
    stats_dict = get_stats(directory)
    print(stats_dict["try"])

    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write(50,"total number of try catch blocks " + str(stats_dict["try"]))
    pdf.ln()
    pdf.output("/Users/jaewookim/PycharmProjects/cs527_project/testings.pdf")



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
            "codeblock":total_num_code_blocks}

detect_main("/Users/jaewookim/PycharmProjects/cs527_project/code-dump/flask-master")


