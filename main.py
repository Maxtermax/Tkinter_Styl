import json
from Tkinter import *



Canvas=Tk()
def Saluda():
	Esneyder["text"]="___________TEXTO CAMBIADO XD_____________" 
	print "Soy", Esneyder["text"]

with open('Style.json') as Archivo_Styl:    
    data= json.load(Archivo_Styl)

Esneyder=Label(Canvas,data["titulo"])
Esneyder.pack(data["pos_titulo"])

boton=Button(Canvas,data["boton"],command=Saluda)
boton.pack()


Canvas.mainloop()


































	









































