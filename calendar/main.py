#http://svn.python.org/projects/sandbox/trunk/ttk-gsoc/samples/ttkcalendar.py
#https://www.youtube.com/watch?v=FrS1lLb4HgA
import sys
from cal import *
from Tkinter import *
import time

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
	alarm.geometry("340x530")
	alarm.geometry("+%d+%d" % (0,0))
	Label(alarm, text="Programar alarma", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(alarm, text="Selecciona dia, hora y compartimiento.", pady= 10).pack()


	DAYS = [
    		"Lunes",
    		"Martes",
    		"Miercoles", 
		"Jueves",
		"Viernes",
		"Sabado",
		"Domingo"
	]
	HOURS = [
		"5:00",
		"6:00",
		"7:00",
		"8:00",
		"9:00",
		"10:00",
		"11:00"
	]
	variable = StringVar(root)
	variable2 = StringVar(root)
	variable.set(DAYS[0])
	variable2.set(HOURS[0])
	w = apply(OptionMenu, (alarm, variable) + tuple(DAYS)).pack()
	w2 = apply(OptionMenu, (alarm, variable2) + tuple(HOURS)).pack()
	#Checkvar
	cv1 = IntVar()
	cv2 = IntVar()
	cv3 = IntVar()
	cv4 = IntVar()
	cv5 = IntVar()

	c1 = Checkbutton(alarm, text = "Compartimiento 1", variable = cv1, onvalue = 1, offvalue = 0, height=2).pack()
	c2 = Checkbutton(alarm, text = "Compartimiento 1", variable = cv2, onvalue = 1, offvalue = 0, height=2).pack()
	c3 = Checkbutton(alarm, text = "Compartimiento 1", variable = cv3, onvalue = 1, offvalue = 0, height=2).pack()
	c4 = Checkbutton(alarm, text = "Compartimiento 1", variable = cv4, onvalue = 1, offvalue = 0, height=2).pack()
	c5 = Checkbutton(alarm, text = "Compartimiento 1", variable = cv5, onvalue = 1, offvalue = 0, height=2).pack()

	guardar = Button(alarm, text="Guardar alarma", fg="white", bg="blue").pack()

	Label(alarm, text="___________________________________________", fg="black", pady=10).pack()	
	salir = Button(alarm, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(alarm)).pack()
	

def days():
	days = Tkinter.Toplevel(root)
	days.geometry("340x530")
	days.geometry("+%d+%d" % (0,0))
	Label(days, text="Reprogramar Pastillero", font=("bold", 12, ), fg="blue", pady= 10).pack()
	Label(days, text="Selecciona uno de los 5 compartimientos", pady= 10).pack()
	btn1 = Button(days, text="Compartimiento 1", fg="white", bg="green3", pady="25", command = c1).pack()
	btn2 = Button(days, text="Compartimiento 2", fg="white", bg="deep sky blue", pady="25", command = c2).pack()
	btn3 = Button(days, text="Compartimiento 3", fg="white", bg="red", pady="25", command = c3).pack()
	btn4 = Button(days, text="Compartimiento 4", fg="white", bg="blue violet", pady="25", command = c4).pack()
	btn5 = Button(days, text="Compartimiento 5", fg="white", bg="black", pady="25", command = c5).pack()
	Label(days, text="___________________________________________", fg="black", pady=10).pack()	
	salir = Button(days, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(days)).pack()

def c1():
	c1= Tkinter.Toplevel(root)
	c1.geometry("340x530")
	c1.geometry("+%d+%d" % (0,0))
	Label(c1, text="___________________________________________", fg="black", pady=10).pack()
	salir = Button(c1, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c1)).pack()

def c2():
	c2= Tkinter.Toplevel(root)
	c2.geometry("340x530")
	c2.geometry("+%d+%d" % (0,0))
	Label(c2, text="___________________________________________", fg="black", pady=10).pack()
	salir = Button(c2, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c2)).pack()

def c3():
	c3= Tkinter.Toplevel(root)
	c3.geometry("340x530")
	c3.geometry("+%d+%d" % (0,0))
	Label(c3, text="___________________________________________", fg="black", pady=10).pack()
	salir = Button(c3, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c3)).pack()

def c4():
	c4= Tkinter.Toplevel(root)
	c4.geometry("340x530")
	c4.geometry("+%d+%d" % (0,0))
	Label(c4, text="___________________________________________", fg="black", pady=10).pack()
	salir = Button(c4, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c4)).pack()

def c5():
	c5= Tkinter.Toplevel(root)
	c5.geometry("340x530")
	c5.geometry("+%d+%d" % (0,0))
	Label(c5, text="___________________________________________", fg="black", pady=10).pack()
	salir = Button(c5, text="Regresar", fg="white", bg="blue", command= lambda: exitFunction(c5)).pack()

def exitFunction(self):
	self.destroy()


#Main
root=Tk()
root.title('Timencan')
root.geometry("340x530")
root.geometry("+%d+%d" % (0,0))
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
btn1 = Button(root, text="Reprogramar pastillero",  fg="white", bg="blue", command = days).pack()
btn2 = Button(root, text="      Agregar alarma      ",  fg="white", bg="blue",command = alarm).pack()
btn3 = Button(root, text="      Ver mis horarios     ", fg="white", bg="blue").pack()

mainloop()
