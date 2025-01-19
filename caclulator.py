"""
File: Calculator
Author: Tyler Delagardelle
Description: A simple calculator.
"""

from tkinter import *
import tkinter
from tkinter import font


#set up the window
root = Tk()
root.title("Calculator")
root.geometry("225x525")


#memory
memString = ""

#functions
def updateDisplay():
    displayBox["text"] = memString

def addition():
    global memString
    if "+" not in memString and "-" not in memString and "*" not in memString and  "/" not in memString:
        memString = memString + "+"
        updateDisplay()
    else:
        displayBox["text"] = "error"

def subtraction():
    global memString
    if "+" not in memString and "-" not in memString and "*" not in memString and  "/" not in memString:

        memString = memString + "-"
        updateDisplay()

    else:
        displayBox["text"] = "error"

def multiply():
    global memString
    if "+" not in memString and "-" not in memString and "*" not in memString and  "/" not in memString:
    
        memString = memString + "*"
        updateDisplay()

    else:
        displayBox["text"] = "error"

def divide():
    global memString
    if "+" not in memString and "-" not in memString and "*" not in memString and  "/" not in memString:

        memString = memString + "/"
        updateDisplay()

    else:
        displayBox["text"] = "error"

def One():
    global memString
    memString = memString + "1"
    updateDisplay()

def Two():
    global memString
    memString = memString + "2"
    updateDisplay()

def Three():
    global memString
    memString = memString + "3"
    updateDisplay()
def Four():
    global memString
    memString = memString + "4"
    updateDisplay()
def Five():
    global memString
    memString = memString + "5"
    updateDisplay()
def Six():
    global memString
    memString = memString + "6"
    updateDisplay()
def Seven():
    global memString
    memString = memString + "7"
    updateDisplay()
def Eight():
    global memString
    memString = memString + "8"
    updateDisplay()
def Nine():
    global memString
    memString = memString + "9"
    updateDisplay()
def Zero():
    global memString
    memString = memString + "0"
    updateDisplay()
def Clear():
    global memString
    memString = ""
    updateDisplay()
def ClearEntry():
    global memString
    memString = ""
    updateDisplay()
def Equals():
    global memString
    memString = str(eval(memString))
    displayBox["text"] = memString
    memString = ""
    
def Negate():
    global memString
    number = eval(memString)
    number = -1 * number
    memString = str(number)
    updateDisplay()
def Decimal():
    global memString
    memString = memString + "."
    updateDisplay()

#font
fontTuple = ("Times New Roman" , 20),
#Button Creation

displayBox = Label(root, font = fontTuple , text = "0" ,height = 3 , width = 20 ,bg = "white")
displayBox.grid(row=0 , column = 0, columnspan = 4)

buttonPlusSign = Button(root ,font = fontTuple , text ="+" , height = 3 , width = 4 , command = addition)
buttonPlusSign.grid(row=1, column = 0)

buttonMinusSign = Button(root ,font = fontTuple , text ="-" ,height = 3 , width = 4, command = subtraction)
buttonMinusSign.grid(row=1, column = 1)

buttonMultSign = Button(root ,font = fontTuple , text ="x" ,height = 3 , width = 4, command = multiply)
buttonMultSign.grid(row=1, column = 2)

buttonDivSign = Button(root ,font = fontTuple , text ="/" ,height = 3 , width = 4, command = divide)
buttonDivSign.grid(row=1, column = 3)

button1 = Button(root ,font = fontTuple , text ="1" ,height = 3 , width = 4, command =One )
button1.grid(row=4, column = 0)

button2 = Button(root ,font = fontTuple , text ="2" ,height = 3 , width = 4, command =Two )
button2.grid(row=4, column = 1)

button3 = Button(root ,font = fontTuple , text ="3" ,height = 3 , width = 4, command =Three )
button3.grid(row=4, column = 2)

button4 = Button(root ,font = fontTuple , text ="4" ,height = 3 , width = 4, command =Four )
button4.grid(row=3, column = 0)

button5 = Button(root ,font = fontTuple , text ="5" ,height = 3 , width = 4, command =Five )
button5.grid(row=3, column = 1)

button6 = Button(root ,font = fontTuple , text ="6" ,height = 3 , width = 4, command =Six )
button6.grid(row=3, column = 2)

button7 = Button(root ,font = fontTuple , text ="7" ,height = 3 , width = 4, command =Seven )
button7.grid(row=2, column = 0)

button8 = Button(root ,font = fontTuple , text ="8" ,height = 3 , width = 4, command =Eight )
button8.grid(row=2, column = 1)

button9 = Button(root ,font = fontTuple , text ="9" ,height = 3 , width = 4, command =Nine )
button9.grid(row=2, column = 2)

button0 = Button(root ,font = fontTuple , text ="0" ,height = 3 , width = 4, command =Zero )
button0.grid(row=5, column = 1)

buttonClear = Button(root ,font = fontTuple , text ="C" ,height = 3 , width = 4, command = Clear )
buttonClear.grid(row=2, column = 3)

buttonClearEntry = Button(root ,font = fontTuple , text ="CE" ,height = 3 , width = 4, command = ClearEntry )
buttonClearEntry.grid(row=3, column = 3)

buttonEquals = Button(root ,font = fontTuple , text= "=" ,height = 7 , width = 4, command =Equals )
buttonEquals.grid(row=4, column = 3, rowspan = 2)

buttonNegate = Button(root ,font = fontTuple , text= "+/-" ,height = 3 , width = 4, command =Negate )
buttonNegate.grid(row=5, column = 0)

buttonDecimal = Button(root ,font = fontTuple , text= "." , height = 3 , width = 4,command =Decimal )
buttonDecimal.grid(row=5, column = 2)


