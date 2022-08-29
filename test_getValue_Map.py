import unittest
from unittest import result
from getValue_Map import getValueMap

class testgetValueMap(unittest.TestCase):
    def test_success(self):
        result = getValueMap('{"x":{"y":{"z":"a"}}}',"x/y/z")
        self.assertEqual(result,"value is : a")
    
    def test_invalidamap(self):
        result = getValueMap("invalidamap","x/y/z")
        self.assertEqual(result,"Error processing the map")
    
    def test_invalidkey(self):
        result = getValueMap('{"x":{"y":{"z":"a"}}}',1)
        self.assertEqual(result,"Key is not a valid string")
    
    def test_novauleinmap(self):
        result = getValueMap('{"x":{"y":{"z":"a"}}}',"x/b/z")
        self.assertEqual(result,"Value Not Found in map")

if __name__ == '__main__':
    unittest.main()