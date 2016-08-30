import unittest
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import timed
from numbers import numero, negativo


class TestNumbers(unittest.TestCase):
    def test_additional(self):
        eq_(numero(25) + numero(24) + negativo(7), 42) #Eq se asegura que los valores sean iguales #number lo pasa a numero, rebmun lo pasa a negativo o vicevera
    def testo(self):
   		ok_(numero(25) + numero(24) + negativo(7), 1000)
    def test_trivial(self):
   	    ok_(numero(25) + numero(24) + negativo(7), 42) #Ok lo hace de manera similar que eq   	    

if __name__ == '__main__':
    unittest.main()

# To run the test suite
# pip install nose
# python tests.py -v
