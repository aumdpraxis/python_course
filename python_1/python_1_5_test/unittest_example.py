import unittest ## pip install unittest2
from my_procedure import *
    
class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOo')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestProc(unittest.TestCase):
    def test_primo(self):
        self.assertEqual(primos(10),[1, 2, 3, 5, 7, 11, 13, 17, 19, 29])

def my_funcion(hola):
    print("hola mundo")


if __name__ == "__main__":
    unittest.main()