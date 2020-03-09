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

def days():
	days = Tkinter.Toplevel(root)
	root.iconify()
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
	w = apply(OptionMenu, (days, variable) + tuple(DAYS))
	w2 = apply(OptionMenu, (days, variable2) + tuple(HOURS))
	w.pack()
	w2.pack()
#	days.parent=days
#	days.parent.protocol("WM_DELETE_WINDOW", upRoot)

def upRoot():
	root.deiconify()

#Main
root=Tk()
root.title('Timencan')
btn1 = Button(root, text="Agregar horario", command = days)

time1 = ''
clock = Label(root, font=('times', 35, 'bold'), bg='white')
clock.pack()

#Call the clock
tick()

#Call calendar widget in cal.py
test()

btn1.pack()
mainloop()
