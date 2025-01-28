from io import open 
import math
#creacion de archivos

texto=open("archivo.txt","w")
texto.write("hola soy un archivo de texto")
texto.write("hola mundo")
texto.close()

#para leer 
lectura=" "
texto=open("archivo.txt","r")
lectura=texto.read()
print(lectura)
texto.close()

