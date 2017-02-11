# -*- coding: utf-8 -*-
import sys

abecedario = map(chr, range(65, 91))

def mostrar(resultado_v,tam):
	muestra = str(resultado_v[0])
	for i in range(1,tam):
		muestra += str(resultado_v[i])
	print ("El resultado es: "+muestra)

def busqueda(letra):
	for i in range(0,len(abecedario)):
		if letra == abecedario[i]:
			return i
def conv(num):
	return abecedario[num]

def clean_(mensaje):

	return mensaje.replace(" ", "")

def tam(mensaje):

	return len(mensaje) - 1
def vigenere(mensaje,clave):
	z = 1
	num_m = busqueda(mensaje[0]) 
	num_c = busqueda(clave[0])
	suma = num_c + num_m
	n_letra = suma % 26
	letra = conv(n_letra)
	cadena = [letra]


	for i in range (1,tam(mensaje)+1):
		num_m = busqueda(mensaje[i]) 
		num_c = busqueda(clave[z])
		z = z +1;

		if z > tam(clave):
			z = 0;
		suma = num_c + num_m
		n_letra = suma % 26
		letra = conv(n_letra)
		cadena += [letra]
	mostrar(cadena,tam(cadena)+1)



def in_datos():
	print("-----------------------------------------------")
	mensaje = raw_input("Incluya la frase a cifrar: ")
	mensaje = str(mensaje)
	mensaje = clean_(mensaje).upper()
	return mensaje

def in_clave():
	print("-----------------------------------------------")
	mensaje = raw_input("Incluya la clave :")
	mensaje = str(mensaje)
	mensaje = clean_(mensaje).upper()
	return mensaje


mensaje = in_datos()
clave = in_clave()
vigenere(mensaje,clave)






