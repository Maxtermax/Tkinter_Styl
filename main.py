import subprocess as comandos
import sys 
from Tkinter import *
import re 


ctx=Tk()


'''
lista=[2,"Indexame",5,50,5]
lista.pop()#saca el ultimo elemento 
lista.pop(1)#saca el elemento de la lista mediante el indice
lista.remove(1)#saca el elemento de la lista mediante el nombre 


lista[0:2]#devuelve un slice desde 0 hasta el index q queramos +1

lista.index("Indexame")#devuelve el indice
lista.insert(0,"Agrega esto despues del indice 0")
lista.count(5)#devuelve cuantas veces se repeti el elemento

lista.sort(reverse=True)

def potenciador(n):
	return n*n
print map(potenciador,[0,34,5])
'''

fs = open("Style.txt","r")
Test=fs.readlines()
fs.close()



def Styl():
	Id=""
	for i in Test:
		if(re.search(":$",i)):
			#find the id 
			Id=i
		elif("color" in i):
			attribute=re.split(" ",i)[1].replace("\n","")
			print attribute #value of the atribute 
			#Add attribute to Tkinter Here.
		elif("background" in i):
			attribute=re.split(" ",i)[1].replace("\n","")
			print attribute #value of the atribute 
			#Add attribute to Tkinter Here.
		
		elif("padding" in i):
			attribute=re.split(" ",i)[1].replace("\n","")
			print attribute #value of the atribute 
			#Add attribute to Tkinter Here.

print Styl()#Como parametro resive el TKinter













	









































