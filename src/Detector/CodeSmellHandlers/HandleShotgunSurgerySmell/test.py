import unittest
import shotgun_surgery as SS

clean = 'sample_shotgun_clean.py'
smelly = 'sample_shotgun_smelly.py'

class TestSmellDetector(unittest.TestCase):

    def test_clean(self):
        res = SS.detect_shotgun_surgery(clean)
        self.assertEqual(res['Customer'][1], False)
        
    def test_smelly(self):
        res = SS.detect_shotgun_surgery(smelly)
        self.assertTrue(res['Customer'][1])
        self.assertTrue(res['Customer2'][1])
if __name__ == '__main__':
    unittest.main()