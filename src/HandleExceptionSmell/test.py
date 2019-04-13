# Python code to illustrate 
# working of try()  
def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional Part as Answer 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ")

    try: 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except: 
        print("An error occurred") 

    try: 
        # Floor Division : Gives only Fractional Part as Answer 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ")
    except NameError: 
        print("Name Error")
    except MemoryError: 
        print("Memory Error")
    except AttributeError: 
        print("Here is some\
            long long error message\
            .....")
  
# Look at parameters and note the working of Program 
divide(3, 0) 