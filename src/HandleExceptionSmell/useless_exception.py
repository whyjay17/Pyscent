# Useless Exception Handling: a try..except statement that does little
# Two types of useless exceptions:
## 1) has only one except clause and catches a too general exception like Exception and Standard Error
## 2) all exception clauses in the statement are empty

# Metrics Needed
## 1) Number of excepts
## 2) Number of General Exception
## 3) Number of empty excepts

# Sources
## 1) https://lignos.org/py_antipatterns/
## 2) https://legacy.python.org/dev/peps/pep-0008/

with open("test.py", "r") as f:
    content = f.readlines()
    print(content)