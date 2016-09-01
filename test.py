import unittest
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import timed
from numbers import numero, negativo

class TestNumbers(unittest.TestCase):	
    def test_additional(self):
        eq_(numero(25) + numero(24) + negativo(7), 42)#Eq se asegura que los valores sean iguales #number lo pasa a numero, rebmun lo pasa a negativo o vicevera 	
    def test_trivial(self):
   	    ok_(numero(25) + numero(24) + negativo(7), 42)#Ok lo hace de manera similar que eq   	    
    def test_resta(self):
        eq_(numero(25) - negativo(numero(24)), 49)
    def test_mult(self):
        ok_(numero(25) * negativo(numero(2)), -50)
    def test_div(self):
        eq_(numero(0) * numero(2), 0) 
    def valores_restringidos(self):
    	eq_(numero(10000),False)
 
     
if __name__ == '__main__':
    unittest.main()

# To run the test suite
# pip install nose
# python tests.py -v
