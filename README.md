# Pyscent
## Project Idea
### Objectives
- Code smell, although often neglected by many programmers, is an important factor that we all should care about to write more maintainable and readable code. Throughout this project, we have discovered that the existing Python smell detectors are not exhaustive enough to cover some code smells that are common in codes written in Python. We have built a wrapper tool, Pyscent, to detect code smells that are not detected by the existing tools. Considering the [report](https://insights.stackoverflow.com/survey/2019) that shows the popularity of Python is higher than ever in the developer community, we expect Pyscent to provide developers a more effective way to detect code smells in their projects. 

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
- astor - Manupulation of Python Source via the AST (https://pypi.org/project/astor)
- matplotlib - Visualization of Code Smell Metrics (https://matplotlib.org)
- subprocess - Subprocess Management (https://docs.python.org/2/library/subprocess.html)
- shlex - Simple Lexcial Analysis (https://docs.python.org/3/library/shlex.html)
- etc.

## Team
- Jaewoo Kim (https://github.com/jaywoo123)
- Yong Jin Kim (https://github.com/whyjay17)
