import os
from matplotlib.pyplot import *
output_list = []

def generate_viz(data,label,filename):
    x_val = []
    y_val = []
    lines = data.splitlines()
    if len(lines) < 2 :
        return
    for idx,line in enumerate(lines):
        line_arr = line.split()
        print(line_arr)
        x_val.append(line_arr[1])
        y_val.append(int(line_arr[5]))
        if idx == 20:
            break
    bar(x_val,y_val)
    xticks(rotation=90)
    xlabel("file names")
    title(filename)
    ylabel(label)
    savefig("../plots/" + filename,bbox_inches = "tight")
    show()



def add_viz():
    for filename in os.listdir("../output/logs/"):
        if filename.endswith("logs") and "exception" not in filename:
            print(filename)
            file_path = "../output/logs/" + filename
            with open(file_path, encoding='UTF8') as f:
                data = f.read()
                if "many" in filename:
                    generate_viz(data,"count",filename)
                if "long" in filename:
                    generate_viz(data,"number of characters",filename)
        # break;


# add_viz("../logs")




