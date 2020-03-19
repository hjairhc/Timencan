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
	w = apply(OptionMenu, (alarm, variable) + tuple(DAYS))
	w2 = apply(OptionMenu, (alarm, variable2) + tuple(HOURS))
	w.pack()
	w2.pack()
	

def days():
	days = Tkinter.Toplevel(root)
	days.geometry("340x530")

def upRoot():
	root.deiconify()

#Main
root=Tk()
root.title('Timencan')
root.geometry("340x530")
#root.wm_attributes("-topmost", 1)

time1 = ''
Label(root, text="Actual Hour", fg="blue", pady= 10).pack()
clock = Label(root, font=('times', 35, 'bold'), bg='white')
clock.pack()

#Call the clock
tick()
Label(root, text="___________________________________________", fg="black", pady=5).pack()
Label(root, text="Calendar", fg="blue", pady= 10).pack()
#Call calendar widget in cal.py
test()
Label(root, text="___________________________________________", fg="black", pady=5).pack()
Label(root, text="Options", fg="blue", pady= 10).pack()
btn1 = Button(root, text="Reprogramar pastillero", command = days).pack()
btn2 = Button(root, text="      Agregar alarma      ", command = alarm).pack()
btn3 = Button(root, text="      Ver mis horarios     ").pack()

mainloop()
