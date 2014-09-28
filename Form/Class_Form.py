from Tkinter import *
root = Tk()

class Form():
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
