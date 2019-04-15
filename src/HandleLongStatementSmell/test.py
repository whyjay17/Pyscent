import unittest
from long_statement import detect_long_lanmbda_function


class TestSmellDetector(unittest.TestCase):

    def test_input_length_35(self):
        self.assertEqual(len(detect_long_lanmbda_function("sample_lambda.py",35)), 1)

    def test_input_length_25(self):
        self.assertEqual(len(detect_long_lanmbda_function("sample_lambda.py", 25)), 3)

    def test_detector_output(self):
        self.assertEqal(detect_long_lanmbda_function("sample_lambda.py", 0),["(test1 = lambda text: (0 if text % 2 == 0 else)",\
                                                                             "(test2 = lambda text: text % 2 == 0)" \
                                                                             "(test3 = lambda text: text %2 == 0)" \
                                                                             ])

if __name__ == '__main__':
    unittest.main()





