# -*- coding: iso-8859-1 -*-

import json
from Tkinter import *
import ttk 
import tkFont



with open('./styles/Style.json') as Archivo_Styl:    
    data= json.load(Archivo_Styl)

root = Tk()
root.geometry("654x350+250+150")

root.maxsize(width=654,height=350)
root.minsize(width=654,height=350)


class Form:
	def __init__(self,root):
		self.root = root #Guarda la instancia principal de TK() dentro de self.root para que pueda se usada en otras funciones

	def Input(self,style,pos,cb):
		self.Input_name=Entry(self.root,style)
		self.Input_name.place(pos)


		return cb(self.Input_name) #cb=callback

		#Retorna el mismo elemento que se crea en la instancia por medio del callback de la funcion que lo maneja
		#Para que se pueda definir una funcion que va a manejar todo lo que tenga que ver con ese elemento			 


	def Button(self,style,pos,cb):
		self.Button_name = Button(self.root,style)
		self.Button_name.place(pos) #Ubica el elemento segun lo que llegue por parametros en el eje x,y
		return cb(self.Button_name)
		#Retorna el mismo elemento que se crea en la instancia por medio del callback de la funcion que lo maneja
		#Para que se pueda definir una funcion que va a manejar todo lo que tenga que ver con ese elemento			 

	def Label(self,style,pos):
		self.Label_name = Label(root,style)
		self.Label_name.place(pos)

	def Run(self,style):
		self.root.config(style)
		self.root.mainloop()








form = Form(root) #Instancia de la clase formulario 





form.Label(data["Title"],data["Title_pos"])
form.Label(data["Uname"],data["Uname_pos"])
form.Label(data["PassU"],data["PassU_pos"])




def Pass_Handler(input=""):
  #Do every you gonna do
  return input#end return the input 



def Name_Handler(input):
  #Do every you gonna do
  return input#end return the input 


def Submit_Handler(btn):
	#validate here if you wanna 
	def Over_Button(event):
		btn.config({"bg":"#016899"})
	#end Over_Button

	def Out_Button(event):
		btn.config({"bg":"#007cb6"})
	#end Out_Button
	
	def validate():
		print name.get() , "Nombre \n"
		name.config(bg="red")
		passW.config(bg="green")
		print passW.get() , "Contraseña"
	
	#end validate 

	#events 
	btn.bind("<Enter>",Over_Button)	
	btn.bind("<Leave>",Out_Button)	
	btn.bind("<FocusIn>",Over_Button)	
	btn.bind("<FocusOut>",Out_Button)	
	btn.config(command=validate)	
	#end events 







passW=form.Input(data["EPass"],data["EPass_pos"],Pass_Handler)

name=form.Input(data["Ename"],data["Ename_pos"],Name_Handler)

form.Button(data["entrar"],data["entrar_pos"],Submit_Handler)




form.Run({"bg":"white"})#config windows 


#http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm 
