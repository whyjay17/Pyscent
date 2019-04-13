def test_lambda():
    # rebind the paint function to implement curriculum learning
        test1 = lambda text: (text %2 == 0)
        test2 = lambda text: \
            text % 2 == 0
        test3 = lambda text: text %2 == 0