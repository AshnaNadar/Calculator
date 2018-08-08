#Ashna Jagadisan
#April 31, 2018
#SUMMARY: Calculator using created using tkinter buttons and functions

from tkinter import *
from math import *

root = Tk()
root.title("Calculator")
root.resizable(0,0)
click = ""
textInput = StringVar()

#Setting variables for colours and padding
#Easier to change colours and paddings for all the buttons
f = ('calibri', 20, 'bold')
w = "white"
blk = "black"
g = "lightgrey"
p = "pink2"
b = 8
pad = 20

#Function enters a number/character on the display when a button is clicked
#Called when a number/character button is clicked, stores string value of button into click and sets screen to display the number/character
def buttonClick(number):
    global click
    click=click+str(number)
    textInput.set(click)

#Function clears display when clear button is clicked
#Called when clear button is clicked, sets screen to display "", clearing the screen
def clearDisplay():
    global click
    click=""
    textInput.set("")

#Function evaluates inputted numbers and performs the required calculation when equal sign is clicked
#Called when equal button is clicked, evaluates the string in the display and outputs the answer
def equalInput():
    global click
    equal=str(eval(click))
    textInput.set(equal)
    click=""

#Calculator's Label
name = Label(text="CALCULATOR", width=14, padx=7, bd=b, bg="white", font=('calibri', 14, 'bold', 'italic'), relief=GROOVE).grid(row=0, column=0, columnspan=4, sticky=W+E)

#Calculator's display screen
def screen():
    display = Entry(root, fg=w, bg=blk, bd=20, font=f, textvariable=textInput, relief=RAISED).grid(row=1,column=0,columnspan=4, sticky=W+E)

#First row of buttons
def rowOne():
    buttonSeven = Button(text="7", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(7)).grid(row=2, column=0)
    buttonEight = Button(text="8", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(8)).grid(row=2, column=1)
    buttonNine = Button(text="9", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(9)).grid(row=2, column=2)
    add = Button(text="+", width=2, padx=7, pady=pad, bd=b, bg=p, font=f, relief=RAISED, command=lambda:buttonClick("+")).grid(row=2, column=3)

#Second row of buttons
def rowTwo():
    buttonFour = Button(text="4", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(4)).grid(row=3, column=0)
    buttonFive = Button(text="5", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(5)).grid(row=3, column=1)
    buttonSix = Button(text="6", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(6)).grid(row=3, column=2)
    subtract = Button(text="-", width=2, padx=7, pady=pad, bd=b, bg=p, font=f, relief=RAISED, command=lambda:buttonClick("-")).grid(row=3, column=3)

#Third row of buttons
def rowThree():
    buttonOne = Button(text="1", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(1)).grid(row=4, column=0)
    buttonTwo = Button(text="2", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(2)).grid(row=4, column=1)
    buttonThree = Button(text="3", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(3)).grid(row=4, column=2)
    multiply = Button(text="*", width=2, padx=7, pady=pad, bd=b, bg=p, font=f, relief=RAISED, command=lambda:buttonClick("*")).grid(row=4, column=3)

#Fourth row of buttons
def rowFour():
    buttonZero = Button(text="0", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(0)).grid(row=5, column=0)
    buttonClear = Button(text="C", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=clearDisplay).grid(row=5, column=1)
    decimal = Button(text=".", width=4, padx=7, pady=pad, bd=b, bg=g, font=f, relief=RAISED, command=lambda:buttonClick(".")).grid(row=5, column=2)
    divide = Button(text="/", width=2, padx=7, pady=pad, bd=b, bg=p, font=f, relief=RAISED, command=lambda:buttonClick("/")).grid(row=5, column=3)

#Fifth row of buttons
def rowFive():
    buttonEqual = Button(text="=", width=14, padx=7, pady=5, bd=b, bg="pink", font=f, relief=RAISED, command=equalInput).grid(row=6, column=0, columnspan=4, sticky=W+E)

screen()
rowOne()
rowTwo()
rowThree()
rowFour()
rowFive()

root.mainloop()
