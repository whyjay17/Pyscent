import unittest
import useless_exception as UE

file_path = 'sample_exception.py'


class TestSmellDetector(unittest.TestCase):

    def test_function(self):
        self.assertEqual(len(UE.detect_useless_exception(file_path)), 8)

    def test_general_exception(self):
        smelly_lines = UE.detect_useless_exception(file_path)
        self.assertTrue(14 in smelly_lines)
        self.assertTrue(62 in smelly_lines)
        
    def test_empty_exception(self):
        smelly_lines = UE.detect_useless_exception(file_path)
        self.assertTrue(35 in smelly_lines)
        self.assertTrue(86 in smelly_lines)

if __name__ == '__main__':
    unittest.main()