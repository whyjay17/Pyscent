import os
from matplotlib.pyplot import *
output_list = []

def generate_viz(data,label,filename):
    x_val = []
    y_val = []
    figure()
    lines = data.splitlines()
    if len(lines) < 2 :
        return
    for idx,line in enumerate(lines):
        line_arr = line.split()
        x_val.append(line_arr[1])
        y_val.append(int(line_arr[5]))
        if idx == 20:
            break
    bar(x_val, y_val, color = "#85b1dd")
    xticks(rotation = 90)
    xlabel("file names")
    title(filename)
    ylabel(label)
    plot_dir = os.path.join("plots")
    if not os.path.exists(os.path.join(plot_dir)):
        os.makedirs(os.path.join(plot_dir))
    
    # filename[:-4] removes .txt to make it readable
    savefig(os.path.join("plots", filename[:-4]), bbox_inches = "tight")

def add_viz():
    for filename in os.listdir(os.path.join("output", "logs")):
        if filename.endswith("logs.txt") and "exception" not in filename:
            file_path = os.path.join("output", "logs", filename)
            with open(file_path, encoding='UTF8') as f:
                data = f.read()
                if "many" in filename:
                    generate_viz(data,"count", filename)
                elif "long" in filename:
                    generate_viz(data,"number of characters", filename)
