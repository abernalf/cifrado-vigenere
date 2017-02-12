#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

abecedario = map(chr, range(65, 91))
abecedario2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def mostrar(resultado_v,tam):
	muestra = str(resultado_v[0])
	for i in range(1,tam):
		muestra += str(resultado_v[i])
	print ("El resultado es: "+muestra)

def busqueda(letra):
	for i in range(0,len(abecedario2)):
		if letra == abecedario2[i]:
			return i
def conv(num):
	return abecedario2[num]

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
def des_vigenere(clave,mensaje):
	z = 1
	num_m = busqueda(mensaje[0]) 
	num_c = busqueda(clave[0])
	resta = num_m - num_c
	if resta < 0:
		resta = resta + 26
	letra = conv(resta)
	cadena = [letra]

	for i in range (1,tam(mensaje)+1):
		num_m = busqueda(mensaje[i]) 
		num_c = busqueda(clave[z])
		z = z +1;
		if z > tam(clave):
			z = 0;
		resta = num_m - num_c
		if resta < 0:
			resta = resta + 26
		letra = conv(resta)
		cadena += [letra]
	mostrar(cadena,tam(cadena)+1)




def in_datos():
	print("-----------------------------------------------")
	mensaje = input("Incluya la frase a cifrar: ")
	mensaje = str(mensaje)
	mensaje = clean_(mensaje).upper()
	return mensaje

def in_clave():
	print("-----------------------------------------------")
	mensaje = input("Incluya la clave :")
	mensaje = str(mensaje)
	mensaje = clean_(mensaje).upper()
	return mensaje
def in_datos_des():
	print("-----------------------------------------------")
	mensaje = input("Incluya la clave para descifrar: ")
	mensaje = str(mensaje)
	mensaje = clean_(mensaje).upper()
	return mensaje
def in_clave_des():
	print("-----------------------------------------------")
	mensaje = input("Incluya el mensaje a descifrar :")
	mensaje = str(mensaje)
	mensaje = clean_(mensaje).upper()
	return mensaje

w = input("----¿DESEA [C]IFRAR O [D]ESCIFRAR O [S]ALIR----:")
w = w.upper()
if w == 'C':
	mensaje = in_datos()
	clave = in_clave()
	vigenere(mensaje,clave)
if w == 'D':
	clave = in_datos_des()
	mensaje = in_clave_des()
	des_vigenere(clave,mensaje)

	##EJECUTAR CON PYTHON 3








