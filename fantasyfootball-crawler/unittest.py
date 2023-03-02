import unittest
from __main__ import *
class TestStringMethods(unittest.TestCase):
    
    def test_ffl_empipty(self):
        ffl_results = read_ffl()
        self.assertTrue(len(ffl_results) != 0)

    def test_pff_empty(self):
        pff_results = read_pff()
        self.assertTrue(len(pff_results) != 0)
    
    def test_next_gen(self):
        nextgen_result = read_nextgen()
        self.assertTrue(len(nextgen_result) != 0)

    def test_dict(self):
        dict_result = get_Dict()
        self.assertTrue(len(dict_result) != 0)

    def test_read_dict(self):
        read_dict_result = read_dict()
        self.assertTrue(len(read_dict_result) != 0)
    
if __name__ == '__main__':
    unittest.main()