import sys
import warnings 

__version__ = '1.0'

# numbers.py Se basa en pasar los valores a numeros o numeros negativos para luego operar
#con ellos con pruebas unitarias
def numero(value):
    if value > sys.maxsize: #Cambiando maxint por maxsize
        print(str(value) + " el numero es muy largo")
        return False
    elif value > 8000:
    	print(str(value) + " Es mas de 8000!")
    	return False
    return int(value)    


def negativo(value):
    return - numero(value)
    
#Creando una prueba simple del programa
def prueba():
	print("Hola, a continuacion de 2 numeros separados por un SPACE")
	x=input()
	x.split(" ")
	n=x[0]
	m=x[2]
	print("Sus numeros son: " + str(n) +" "+ str(m))
	print ("Selecciones una operacion simple")
	print ("Suma: s // Resta: r // Multiplicacion: m // Division: d")
	o=input()
	if str(o) == "s":
		x= numero(int(n)+int(m))
	if str(o) == "r":
		x= numero(int(n)-int(m))
	if str(o) == "m":
		x= numero(int(n)*int(m))
	if str(o) == "d":
		if int(m)!=0:
			x= numero(int(n)/int(m))
		else:
			print("El divisor no puede ser cero")
	return x
	
print(prueba())

def leet():
    return 31337



