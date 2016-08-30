import sys
import warnings 

__version__ = '1.0'
print("hola")

# numbers.py Se basa en pasar los valores a numeros o numeros negativos para luego operar
#con ellos con pruebas unitarias
def numero(value):
    if value > sys.maxsize: #Cambiando maxint por maxsize
        print(str(value) + " el numero es muy largo")
        warnings.warn('.__.')
        return False
    elif value > 8000:
    	print(str(value) + " Es mas de 8000!")
    	warnings.warn('.__.')
    	return False
    return int(value)


def negativo(value):
    return - number(value)
    
#Creando una prueba simple del programa
def prueba():
	print("Hola, a continuacion de 2 numeros")
	n=input()
	m=input()
	print("Sus numeros son: " + str(n) +" "+ str(m))
	print ("Selecciones una operacion simple")
	print ("Suma: s // Resta: r // Multiplicacion: m // Division: d")
	o=input()
	if str(o) == "s":
		print( numero(int(n)+int(m)))
	if str(o) == "r":
		print( numero(int(n)-int(m)))
	if str(o) == "m":
		print( numero(int(n)*int(m)))
	if str(o) == "d":
		if int(m)!=0:
			print( numero(int(n)/int(m)))

prueba()

def leet():
    return 31337



