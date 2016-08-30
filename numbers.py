import sys
import warnings 

__version__ = '1.0'

warnings.warn('You are an idiot')
print("hey lenguage!")

def number(value):
    if value > sys.maxsize: #Cambiando maxint por maxsize
        print(str(value) + " long int is long")
        warnings.warn('.__.')
        return False
    elif value > 9000:
    	print(str(value) + " It\'s over 9000!")
    	warnings.warn('.__.')
    	return False
    return int(value)


def rebmun(value):
    return - number(value)


def leet():
    return 31337
