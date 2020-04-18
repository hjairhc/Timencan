import sys
import os
from cal import *
from Tkinter import *
from tkMessageBox import *
import tkMessageBox
import time
from threading import Timer
import os

#Function for the clock in the main page.
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)

def alarm():
	alarm = Tkinter.Toplevel(root)
	alarm.geometry("340x530+0+0")
	Label(alarm, text="Programar alarma", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(alarm, text="Selecciona dia.", pady= 6).pack()

	DAYS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo" ]
	HOURS = ["5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00",
				"14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",
				 "22:00", "23:00", "24:00" ]
	variable = StringVar(root)
	variable2 = StringVar(root)
	variable.set(DAYS[0])
	variable2.set(HOURS[0])
	w = apply(OptionMenu, (alarm, variable) + tuple(DAYS)).pack()
	Label(alarm, text="Selecciona hora.", pady= 6).pack()
	w2 = apply(OptionMenu, (alarm, variable2) + tuple(HOURS)).pack()
	#Checkvar
	cv1 = IntVar()
	cv2 = IntVar()
	cv3 = IntVar()
	cv4 = IntVar()
	cv5 = IntVar()
	Label(alarm, text="Selecciona compartimiento.", pady= 6).pack()
	c1 = Checkbutton(alarm, text = "Compartimiento 1", variable = cv1, onvalue = 1, offvalue = 0, height=2, bg="green3", fg="gray").pack()
	c2 = Checkbutton(alarm, text = "Compartimiento 2", variable = cv2, onvalue = 1, offvalue = 0, height=2, bg="deep sky blue", fg="gray").pack()
	c3 = Checkbutton(alarm, text = "Compartimiento 3", variable = cv3, onvalue = 1, offvalue = 0, height=2, bg="red", fg="gray").pack()
	c4 = Checkbutton(alarm, text = "Compartimiento 4", variable = cv4, onvalue = 1, offvalue = 0, height=2, bg="blue violet", fg="gray").pack()
	c5 = Checkbutton(alarm, text = "Compartimiento 5", variable = cv5, onvalue = 1, offvalue = 0, height=2, bg="black", fg="gray").pack()

	Label(alarm, text="", fg="black", pady=0).pack() 
	guardar = Button(alarm, text="Guardar alarma", fg="white", bg="blue", command= lambda: saveAlarm(alarm, variable.get(), variable2.get(), cv1.get(), cv2.get(), cv3.get(), cv4.get(), cv5.get())).pack()

	Label(alarm, text="___________________________________________", fg="black", pady=8).pack()	
	salir = Button(alarm, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(alarm)).pack()
	

def days():
	days = Tkinter.Toplevel(root)
	days.geometry("340x530+0+0")
	Label(days, text="Reprogramar Pastillero", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(days, text="Selecciona uno de los 5 compartimientos", pady= 10).pack()
	btn1 = Button(days, text="Compartimiento 1", fg="white", bg="green3", pady="25", command = c1).pack()
	btn2 = Button(days, text="Compartimiento 2", fg="white", bg="deep sky blue", pady="25", command = c2).pack()
	btn3 = Button(days, text="Compartimiento 3", fg="white", bg="red", pady="25", command = c3).pack()
	btn4 = Button(days, text="Compartimiento 4", fg="white", bg="blue violet", pady="25", command = c4).pack()
	btn5 = Button(days, text="Compartimiento 5", fg="white", bg="black", pady="25", command = c5).pack()
	Label(days, text="___________________________________________", fg="black", pady=10).pack()	
	salir = Button(days, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(days)).pack()

def horarios():
	horarios= Tkinter.Toplevel(root)
	horarios.geometry("340x530+0+0")
	Label(horarios, text="Horarios", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(horarios, text="Compartimiento 1", font=("bold", 10, ), fg="blue", pady= 5).pack()
	f = open ('c1.txt','r')
	mensaje = f.read()
	lim = mensaje.find("\n")
	med = mensaje[0:lim]
	seg = mensaje[lim+1: 30]
	lim2 = seg.find("\n")
	hora = seg[0:lim2]
	ter = mensaje[lim2+lim+2: 30]
	lim3 = ter.find("\n")
	cant = ter[0:lim3]
	Label(horarios, text="Medicina: "+med + "\nHoras: "+hora+"     Pastillas: "+cant, font=("bold", 8, ), bg="white" ,fg="black", pady= 5).pack()
	f.close()

	Label(horarios, text="Compartimiento 2", font=("bold", 10, ), fg="blue", pady= 10).pack()
	f = open ('c2.txt','r')
	mensaje = f.read()
	lim = mensaje.find("\n")
	med = mensaje[0:lim]
	seg = mensaje[lim+1: 30]
	lim2 = seg.find("\n")
	hora = seg[0:lim2]
	ter = mensaje[lim2+lim+2: 30]
	lim3 = ter.find("\n")
	cant = ter[0:lim3]
	Label(horarios, text="Medicina: "+med + "\nHoras: "+hora+"     Pastillas: "+cant, font=("bold", 8, ), bg="white" ,fg="black", pady= 5).pack()
	f.close()	

	Label(horarios, text="Compartimiento 3", font=("bold", 10, ), fg="blue", pady= 10).pack()
	f = open ('c3.txt','r')
	mensaje = f.read()
	lim = mensaje.find("\n")
	med = mensaje[0:lim]
	seg = mensaje[lim+1: 30]
	lim2 = seg.find("\n")
	hora = seg[0:lim2]
	ter = mensaje[lim2+lim+2: 30]
	lim3 = ter.find("\n")
	cant = ter[0:lim3]
	Label(horarios, text="Medicina: "+med + "\nHoras: "+hora+"     Pastillas: "+cant, font=("bold", 8, ), bg="white" ,fg="black", pady= 5).pack()
	f.close()	

	Label(horarios, text="Compartimiento 4", font=("bold", 10, ), fg="blue", pady= 10).pack()
	f = open ('c4.txt','r')
	mensaje = f.read()
	lim = mensaje.find("\n")
	med = mensaje[0:lim]
	seg = mensaje[lim+1: 30]
	lim2 = seg.find("\n")
	hora = seg[0:lim2]
	ter = mensaje[lim2+lim+2: 30]
	lim3 = ter.find("\n")
	cant = ter[0:lim3]
	Label(horarios, text="Medicina: "+med + "\nHoras: "+hora+"     Pastillas: "+cant, font=("bold", 8, ), bg="white" , fg="black", pady= 5).pack()
	f.close()	

	Label(horarios, text="Compartimiento 5", font=("bold", 10, ), fg="blue", pady= 10).pack()
	f = open ('c5.txt','r')
	mensaje = f.read()
	lim = mensaje.find("\n")
	med = mensaje[0:lim]
	seg = mensaje[lim+1: 30]
	lim2 = seg.find("\n")
	hora = seg[0:lim2]
	ter = mensaje[lim2+lim+2: 30]
	lim3 = ter.find("\n")
	cant = ter[0:lim3]
	Label(horarios, text="Medicina: "+med + "\nHoras: "+hora+"     Pastillas: "+cant, font=("bold", 8, ), bg="white" ,fg="black", pady= 5).pack()
	f.close()		

	Label(horarios, text="\n___________________________________________", fg="black", pady=10).pack()
	salir = Button(horarios, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(horarios)).pack()

def c1():
	c1= Tkinter.Toplevel(root)
	c1.geometry("340x530+0+0")
	Label(c1, text="Compartimiento 1", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(c1, text="Llena los datos para programar los horarios.", pady= 10).pack()
	Label(c1, text=" ", fg="black", pady=10).pack()
	Label(c1, text="Nombre del medicamento", fg="black", pady=10).pack()
	v = StringVar()
	Entry(c1, textvariable=v).pack()
	v.set(" ")
	s = v.get()
	Label(c1, text="Intervalo de horas.", fg="black", pady=10).pack()
	NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
	variable = StringVar(c1)
	variable.set(NUM[0])
	w = apply(OptionMenu, (c1, variable) + tuple(NUM)).pack()
	Label(c1, text="Cantidad de pastillas a tomar.", fg="black", pady=10).pack()
	CAN = ["1", "2", "3", "4", "5"]
	cantidad = StringVar(c1)
	cantidad.set(CAN[0])
	w = apply(OptionMenu, (c1, cantidad) + tuple(CAN)).pack()
	Label(c1, text=" ", fg="black", pady=10).pack()
	guardar = Button(c1, text="Guardar alarma", fg="white", bg="blue", command =lambda: saveComp(c1, 1, v.get(), variable.get(), cantidad.get())).pack()
	Label(c1, text="\n\n\n___________________________________________", fg="black", pady=10).pack()
	salir = Button(c1, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c1)).pack()

def c2():
	c2= Tkinter.Toplevel(root)
	c2.geometry("340x530+0+0")
	Label(c2, text="Compartimiento 2", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(c2, text="Llena los datos para programar los horarios.", pady= 10).pack()
	Label(c2, text=" ", fg="black", pady=10).pack()
	Label(c2, text="Nombre del medicamento", fg="black", pady=10).pack()
	v = StringVar()
	Entry(c2, textvariable=v).pack()
	v.set(" ")
	s = v.get()
	Label(c2, text="Intervalo de horas.", fg="black", pady=10).pack()
	NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
	variable = StringVar(c2)
	variable.set(NUM[0])
	w = apply(OptionMenu, (c2, variable) + tuple(NUM)).pack()
	Label(c2, text="Cantidad de pastillas a tomar.", fg="black", pady=10).pack()
	CAN = ["1", "2", "3", "4", "5"]
	cantidad = StringVar(c2)
	cantidad.set(CAN[0])
	w = apply(OptionMenu, (c2, cantidad) + tuple(CAN)).pack()
	Label(c2, text=" ", fg="black", pady=10).pack()
	guardar = Button(c2, text="Guardar alarma", fg="white", bg="blue", command =lambda: saveComp(c2, 2, v.get(), variable.get(), cantidad.get())).pack()
	Label(c2, text="\n\n\n___________________________________________", fg="black", pady=10).pack()
	salir = Button(c2, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c2)).pack()

def c3():
	c3= Tkinter.Toplevel(root)
	c3.geometry("340x530+0+0")
	Label(c3, text="Compartimiento 3", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(c3, text="Llena los datos para programar los horarios.", pady= 10).pack()
	Label(c3, text=" ", fg="black", pady=10).pack()
	Label(c3, text="Nombre del medicamento", fg="black", pady=10).pack()
	v = StringVar()
	Entry(c3, textvariable=v).pack()
	v.set(" ")
	s = v.get()
	Label(c3, text="Intervalo de horas.", fg="black", pady=10).pack()
	NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
	variable = StringVar(c3)
	variable.set(NUM[0])
	w = apply(OptionMenu, (c3, variable) + tuple(NUM)).pack()
	Label(c3, text="Cantidad de pastillas a tomar.", fg="black", pady=10).pack()
	CAN = ["1", "2", "3", "4", "5"]
	cantidad = StringVar(c3)
	cantidad.set(CAN[0])
	w = apply(OptionMenu, (c3, cantidad) + tuple(CAN)).pack()
	Label(c3, text=" ", fg="black", pady=10).pack()
	guardar = Button(c3, text="Guardar alarma", fg="white", bg="blue", command =lambda: saveComp(c3, 3, v.get(), variable.get(), cantidad.get())).pack()
	Label(c3, text="\n\n\n___________________________________________", fg="black", pady=10).pack()
	salir = Button(c3, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c3)).pack()

def c4():
	c4= Tkinter.Toplevel(root)
	c4.geometry("340x530+0+0")
	Label(c4, text="Compartimiento 4", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(c4, text="Llena los datos para programar los horarios.", pady= 10).pack()
	Label(c4, text=" ", fg="black", pady=10).pack()
	Label(c4, text="Nombre del medicamento", fg="black", pady=10).pack()
	v = StringVar()
	Entry(c4, textvariable=v).pack()
	v.set(" ")
	s = v.get()
	Label(c4, text="Intervalo de horas.", fg="black", pady=10).pack()
	NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
	variable = StringVar(c4)
	variable.set(NUM[0])
	w = apply(OptionMenu, (c4, variable) + tuple(NUM)).pack()
	Label(c4, text="Cantidad de pastillas a tomar.", fg="black", pady=10).pack()
	CAN = ["1", "2", "3", "4", "5"]
	cantidad = StringVar(c4)
	cantidad.set(CAN[0])
	w = apply(OptionMenu, (c4, cantidad) + tuple(CAN)).pack()
	Label(c4, text=" ", fg="black", pady=10).pack()
	guardar = Button(c4, text="Guardar alarma", fg="white", bg="blue", command =lambda: saveComp(c4, 4, v.get(), variable.get(), cantidad.get())).pack()
	Label(c4, text="\n\n\n___________________________________________", fg="black", pady=10).pack()
	salir = Button(c4, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c4)).pack()

def c5():
	c5= Tkinter.Toplevel(root)
	c5.geometry("340x530+0+0")
	Label(c5, text="Compartimiento 5", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(c5, text="Llena los datos para programar los horarios.", pady= 10).pack()
	Label(c5, text=" ", fg="black", pady=10).pack()
	Label(c5, text="Nombre del medicamento", fg="black", pady=10).pack()
	v = StringVar()
	Entry(c5, textvariable=v).pack()
	Label(c5, text="Intervalo de horas.", fg="black", pady=10).pack()
	NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
	variable = StringVar(c5)
	variable.set(NUM[0])
	w = apply(OptionMenu, (c5, variable) + tuple(NUM)).pack()
	Label(c5, text="Cantidad de pastillas a tomar.", fg="black", pady=10).pack()
	CAN = ["1", "2", "3", "4", "5"]
	cantidad = StringVar(c5)
	cantidad.set(CAN[0])
	w = apply(OptionMenu, (c5, cantidad) + tuple(CAN)).pack()
	Label(c5, text=" ", fg="black", pady=10).pack()
	guardar = Button(c5, text="Guardar alarma", fg="white", bg="blue", command =lambda: saveComp(c5, 5, v.get(), variable.get(), cantidad.get())).pack()
	Label(c5, text="\n\n\n___________________________________________", fg="black", pady=10).pack()
	salir = Button(c5, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c5)).pack()

def exitFunction(ventana):
	ventana.destroy()

def saveComp(self, compartimiento, medicamento, hora, cant):
	conf= Tkinter.Toplevel(root)
	conf.geometry("340x530+0+0")
	Label(conf, text="\n\n\n\n\n\n\n\n\n\nGuardar los cambios", fg="black", pady=10).pack()
	conf.wm_attributes("-topmost", 1)
	confirmar = Button(conf, text="Confirmar", fg="white", bg="blue", pady="15", command =lambda: compCerrar(self, conf, compartimiento, medicamento, hora, cant)).pack()
	cancelar = Button(conf, text="Cancelar", fg="white", bg="blue", pady="15", command=lambda: exitFunction(conf)).pack()	
	

def compCerrar(conf, self, compartimiento, medicamento, hora, cant):
	writeFile(compartimiento, medicamento, hora, cant)
	#Abrir CompartimientoFisico(compartimiento)
	temporizador(compartimiento, medicamento, hora, cant)
	self.destroy()
	conf.destroy()	

def temporizador(compartimiento, medicamento, hora, cant):
	tiempo = int(hora)*2# * 3600;
	t = Timer(tiempo, lambda: timeout(hora, compartimiento, medicamento, cant))
	t.start()
	#timeout(hora, compartimiento, medicamento, cant)
	
	
def timeout(hora, compartimiento, medicamento, cant):
	tim= Tkinter.Toplevel()
	tim.geometry("340x530+0+0")
	Label(tim, text="Abrir Pastillero", font=("bold", 12), fg="blue", pady= 12).pack()
	Label(tim, text="\n\n\nSe abrira el compartimiento "+ str(compartimiento), font=("bold", 10), fg="black", pady=10).pack()	
	Label(tim, text="Tomar Medicina: ", font=("bold", 10), fg="black", pady=10).pack()
	Label(tim, text=medicamento, font=("bold", 10), bg="white", fg="black", pady=10).pack()
	Label(tim, text="Tu dosis son: ", font=("bold", 10), fg="black", pady=10).pack()
	Label(tim, text=cant + " Pastillas", font=("bold", 10), fg="black", bg="white", pady=10).pack()
	Label(tim, text="\n\n\n___________________________________________", fg="black", pady=10).pack()
	abrir = Button(tim, text="Abrir pastillero", fg="white", bg="blue", pady="10", command =lambda: cerrarPastillero(tim, hora, compartimiento, medicamento, cant)).pack()
	
def cerrarPastillero(tim, hora, compartimiento, medicamento, cant):
	tim.destroy()
	clos= Tkinter.Toplevel(root)
	clos.geometry("340x530+0+0")
	Label(clos, text="Cerrar Pastillero", font=("bold", 12), fg="blue", pady= 12).pack()
	Label(clos, text="\n\n\n\n\n\nSe cerrara el compartimiento "+ str(compartimiento), font=("bold", 10), fg="black", pady=10).pack()	
	Label(clos, text="La siguiente alarma es en: ", font=("bold", 10), fg="black", pady=10).pack()
	Label(clos, text=hora+" horas.", font=("bold", 10), bg="white",fg="black", pady=10).pack()	
	Label(clos, text="\n\n\n___________________________________________", fg="black", pady=10).pack()
	abrir = Button(clos, text="Cerrar Pastillero", fg="white", bg="blue", pady="10", command =lambda: reiniciarTimer(clos, hora, compartimiento, medicamento, cant)).pack()	

def reiniciarTimer(clos, hora, compartimiento, medicamento, cant):
	clos.destroy()
	tiempo = int(hora)*2# * 3600;
	t = Timer(tiempo, lambda: timeout(hora, compartimiento, medicamento, cant))
	t.start()

def writeFile(comp, med, hora, cant):
	lineas = [med, hora, cant]
	dirFichero='c%d.txt' %comp
	fichero = open(dirFichero, 'w')	
	for l in lineas:
		fichero.write(l+"\n")
	fichero.close() 

def saveAlarm(self, dia, hora, c1, c2, c3, c4, c5):
	conf= Tkinter.Toplevel(root)
	conf.geometry("340x530+0+0")
	conf.wm_attributes("-topmost", 1)
	Label(conf, text="\n\n\n\n\n\n\n\n\n\nGuardar los cambios", fg="black", pady=10).pack()
	conf.wm_attributes("-topmost", 1)
	confirmar = Button(conf, text="Confirmar", fg="white", bg="blue", pady="15", command =lambda: escribirAlarma(self, conf, dia, hora, c1, c2, c3, c4, c5)).pack()
	cancelar = Button(conf, text="Cancelar", fg="white", bg="blue", pady="15", command=lambda: exitFunction(conf)).pack()	

def escribirAlarma(conf, self, dia, hora, c1, c2, c3, c4, c5):
	writeAlarm(dia, hora, c1, c2, c3, c4, c5)
	self.destroy()
	conf.destroy()

def writeAlarm(dia, hora, c1, c2, c3, c4, c5):	
	lineas = [dia, hora, str(c1), str(c2), str(c3), str(c4), str(c5)]
	dirFichero='alarmas.txt'
	fichero = open(dirFichero, 'a+')	
	for l in lineas:
		fichero.write(l+"\n")
	fichero.write("\n")
	fichero.close() 
		

#Main
root=Tk()
root.title('Timencan')
root.geometry("340x530")
root.geometry("+%d+%d" % (0,0))
#root.overrideredirect(1)
#root.wm_attributes("-topmost", 1)
time1 = ''
Label(root, text="Hora actual", fg="blue", font=("bold", 12), pady= 5).pack()
clock = Label(root, font=('times', 35, 'bold'), bg='white')
clock.pack()

#Call the clock
tick()
Label(root, text="___________________________________________", fg="black", pady=5).pack()
Label(root, text="Calendario", fg="blue", font=("bold", 12), pady= 5).pack()
#Call calendar widget in cal.py
test()
Label(root, text="___________________________________________", fg="black", pady=5).pack()
Label(root, text="Opciones", fg="blue", font=("bold", 12), pady= 5).pack()
btn1 = Button(root, text="Reprogramar pastillero",  fg="white", bg="blue", pady="8", command = days).pack()
btn2 = Button(root, text="      Agregar alarma      ",  fg="white", bg="blue", pady="8",command = alarm).pack()
btn3 = Button(root, text="      Ver mis horarios     ", fg="white", bg="blue", pady="8", command = horarios).pack()

mainloop()
