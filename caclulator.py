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
    #updates display
    displayBox["text"] = memString

def addition():
    global memString
    #makes sure that you are creating a viable eqaution to evaluate, ignoring the first character in case of negative
    if "+" not in memString[1:] and "-" not in memString[1:] and "*" not in memString[1:] and  "/" not in memString[1:]:
        #adds "+" to memString
        memString = memString + "+"
        updateDisplay()
    else:
         #if there was already an operand in the string, displays error
        displayBox["text"] = "error"

def subtraction():
    global memString
    #makes sure that you are creating a viable eqaution to evaluate, ignoring the first character in case of negative
    if "+" not in memString[1:] and "-" not in memString[1:] and "*" not in memString[1:] and  "/" not in memString[1:]:
        #adds '-' to memString
        memString = memString + "-"
        updateDisplay()

    else:
        #if there was already an operand in the string, displays error
        displayBox["text"] = "error"

def multiply():
    global memString
    #makes sure that you are creating a viable eqaution to evaluate, ignoring the first character in case of negative
    if "+" not in memString[1:] and "-" not in memString[1:] and "*" not in memString[1:] and  "/" not in memString[1:]:
        #adds '*' to memString
        memString = memString + "*"
        updateDisplay()

    else:
        #if there was already an operand in the string, displays error
        displayBox["text"] = "error"

def divide():
    global memString
    #makes sure that you are creating a viable eqaution to evaluate, ignoring the first character in case of negative
    if "+" not in memString[1:] and "-" not in memString[1:] and "*" not in memString[1:] and  "/" not in memString[1:]:
         #adds '/' to memString
        memString = memString + "/"
        updateDisplay()

    else:
         #if there was already an operand in the string, displays error
        displayBox["text"] = "error"

def One():
    global memString
    #adds "1" to end of mem string, then updates display
    memString = memString + "1"
    updateDisplay()

def Two():
    global memString
    #adds "2" to end of mem string, then updates display
    memString = memString + "2"
    updateDisplay()

def Three():
    global memString
    #adds "3" to end of mem string, then updates display
    memString = memString + "3"
    updateDisplay()
def Four():
    global memString
    #adds "4" to end of mem string, then updates display
    memString = memString + "4"
    updateDisplay()
def Five():
    global memString
    #adds "5" to end of mem string, then updates display
    memString = memString + "5"
    updateDisplay()
def Six():
    global memString
    #adds "6" to end of mem string, then updates display
    memString = memString + "6"
    updateDisplay()
def Seven():
    global memString
    #adds "7" to end of mem string, then updates display
    memString = memString + "7"
    updateDisplay()
def Eight():
    global memString
    #adds "8" to end of mem string, then updates display
    memString = memString + "8"
    updateDisplay()
def Nine():
    global memString
    #adds "9" to end of mem string, then updates display
    memString = memString + "9"
    updateDisplay()
def Zero():
    global memString
    #adds "0" to end of mem string, then updates display
    memString = memString + "0"
    updateDisplay()
def Clear():
    #clears memory and updates display
    global memString
    memString = ""
    updateDisplay()
def ClearEntry():
     #clears memory and updates display
    global memString
    memString = ""
    updateDisplay()
def Equals():
    global memString
    #evaluates memory string
    memString = str(eval(memString))
    #displays memory string
    displayBox["text"] = memString
    #clears memory
    memString = ""
    
def Negate():
    global memString
    #Checks to see if there is an operand or not
    if "+" not in memString[1:] and "-" not in memString[1:] and "*" not in memString[1:] and  "/" not in memString[1:]:
        #if no operand, then can just negate current memString, then updates display
        number = eval(memString)
        number = -1 * number
        memString = str(number)
        updateDisplay()
        
    else:
        #if there is an operand, finds the index of the operand
        if "+" in memString:
            index = memString.index("+")
        elif "-" in memString:
            index = memString.index("-")
        elif "*" in memString:
            index = memString.index("*")
        else:
            index = memString.index("/")
        #slices the string into the first number+operand, and second number
        memSlice = memString[index+1:]
        memSlice1 = memString[:index+1]
        #negates second number
        negateNum =str(-1 * eval(memSlice))
        #combines the strings back together
        memString = memSlice1 + negateNum
        #updaste display
        updateDisplay()
        
        
def Decimal():
    global memString
    #adds a decimal to memString
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


