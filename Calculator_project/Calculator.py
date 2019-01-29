#Calculator Program

import tkinter as tk
from tkinter import *

mainWindow =tk.Tk()
mainWindow.title("CALCULATOR")
mainWindow.geometry('500x400+300+100')

heading_label =tk.Label(mainWindow,text="Simple Calculator:\n",fg="red",font=("Algerian",20,"italic","bold"))
heading_label.grid(row=0,column=6)

heading_label3 =tk.Label(mainWindow,text="First Number",fg="blue" )
heading_label3.grid(row=2,column=2,pady=(0,10))

first_number =tk.Entry(mainWindow)
first_number.grid(row=2,column=6,pady=(0,10))

heading_label2 =tk.Label(mainWindow,text="Second Number",fg="blue" )
heading_label2.grid(row=3,column=2,pady=(0,10))

Second_number =tk.Entry(mainWindow)
Second_number.grid(row=3,column=6,pady=(0,10))

heading_label1 =tk.Label(mainWindow,text="Addition : " )
heading_label1.grid(row=5,column=2,pady=(0,10))

def addition():
    value1 = first_number.get()
    value2 = Second_number.get()

    try:
        first = float(value1)
        second = float(value2)
        if (second != 0):
            result = first + second
            print('Addition Result is: ', result,"\n")

        else:
            print('\nValue of Second Variable cannot be zero.')
    except:
        print("\nPlease enter integer values only.")

def subtraction():
    value1=first_number.get()
    value2=Second_number.get()
    try:
        first = float(value1)
        second = float(value2)
        if (second != 0):
            result = first - second
            print('Subtraction Result is: ', result,"\n")

        else:
            print('\nValue of Second Variable cannot be zero.')


    except:
        print("\nPlease enter integer values only.")

def multiplication():
    value1 = first_number.get()
    value2 = Second_number.get()
    try:
        first = float(value1)
        second = float(value2)
        if (second != 0):
            result = first * second
            print('Multiplication Result is: ', result,"\n")

        else:
            print('\nValue of Second Variable cannot be zero.')


    except:
        print("\nPlease enter integer values only.")

def division():
    value1 = first_number.get()
    value2 = Second_number.get()
    try:
        first = float(value1)
        second = float(value2)
        if (second != 0):
            result = first / second
            print('Division Result is: ', result,"\n")

        else:
           print('\nValue of Second Variable cannot be zero.')


    except:
        print("\nPlease enter integer values only.")

def modulus():
    value1 = first_number.get()
    value2 = Second_number.get()
    try:
        first = float(value1)
        second = float(value2)
        if (second != 0):
            result = first % second
            print('Modulus Result is: ', result,"\n")

        else:
            print('\nValue of Second Variable cannot be zero.')


    except:
        print('\nPlease enter integer values only.')

button1= tk.Button(mainWindow,text=" + ",bg="cyan",command=lambda: addition())
button1.grid(row=5,column=5,pady=(0,10))

heading_label4 =tk.Label(mainWindow,text="Subtraction : " )
heading_label4.grid(row=6,column=2,pady=(0,10))

button2= tk.Button(mainWindow,text=" - ",bg="cyan",command=lambda: subtraction())
button2.grid(row=6,column=5,pady=(0,10))

heading_label5 =tk.Label(mainWindow,text="Multiplication : " )
heading_label5.grid(row=7,column=2,pady=(0,10))

button3= tk.Button(mainWindow,text=" * ",bg="cyan",command=lambda: multiplication())
button3.grid(row=7,column=5,pady=(0,10))

heading_label6 =tk.Label(mainWindow,text="Division : " )
heading_label6.grid(row=8,column=2,pady=(0,10))

button4= tk.Button(mainWindow,text=" / ",bg="cyan",command=lambda: division())
button4.grid(row=8,column=5,pady=(0,10))

heading_label7 =tk.Label(mainWindow,text="Modulus : " )
heading_label7.grid(row=9,column=2,pady=(0,10))

button5= tk.Button(mainWindow,text=" % ",bg="cyan",command=lambda: modulus())
button5.grid(row=9,column=5,pady=(0,10))


def clear():
    first_number.delete('0', tk.END)
    Second_number.delete('0', tk.END)


button5= tk.Button(mainWindow,text=" Reset ",bg="cyan",fg="red",command=lambda: clear())
button5.grid(row=8,column=6,pady=(0,10))

mainWindow.mainloop()