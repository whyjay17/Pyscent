# Python code to illustrate 
# working of try()  
def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional Part as Answer 
        result = x // y 
        test_lambda(aaa)
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError:
        test_lambda()
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
    try: 
        # Floor Division : Gives only Fractional Part as Answer 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        pass
    except NameError: 
        pass
    except MemoryError: 
        print("Memory Error")
    except AttributeError: 
        pass
    
def test_lambda():
    # rebind the paint function to implement curriculum learning
        return lambda text: (0 if text % 2 == 0 else
                              1)
        test2 = lambda text: \
            text % 2 == 0
        test3 = lambda text: text %2 == 0
# Look at parameters and note the working of Program 
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
    
try: 
    # Floor Division : Gives only Fractional Part as Answer 
    result = x // y 
    print("Yeah ! Your answer is :", result) 
except ZeroDivisionError: 
    pass
except NameError: 
    pass
except MemoryError: 
    print("Memory Error")
except AttributeError: 
    pass