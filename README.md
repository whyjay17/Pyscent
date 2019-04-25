# CS527 Project
## Project Idea
### Problem Definition
- Detect code smells in Python code
- Find common security issues in Python code
- Survey different candidates of python code analysis tools to see which types of code smells are addressed with tools available
- Compute various metrics from the Python source code
- Help enforce coding standard for Python
- Add additional code smell features to the existing open source tool
- Develop a wrapper tool which summarizes metrics for code smells based on the output of different types of existing tools
- Provide analysis of code smells through data visualization

## Process Flow
![Process Flow](https://i.imgur.com/2HsO83e.png)

## How to Run
- `cd <pyscent_root_directory>`
- `python pyscent.py <path_to_project_to_inspect>`

## Used Tools
### Static Code Analysis Tools
- pylint (https://www.pylint.org)
- pyflakes (https://github.com/PyCQA/pyflakes)
- Radon (https://pypi.org/project/radon/)
- Cohesion (https://github.com/mschwager/cohesion)
### Libraries
- ast — Abstract Syntax Trees (https://docs.python.org/3/library/ast.html)
- etc.

## Team
- Jaewoo Kim (https://github.com/jaywoo123)
- Yong Jin Kim (https://github.com/whyjay17)
