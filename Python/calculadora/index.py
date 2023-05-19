#Author = By Tutos Rive Gamer (TRG)

from tkinter import *


# Declaration Window
window = Tk()
window.title("Calculator TRG")
window['bg'] = "#1a1a1a"
window.title("TRG Calculator")
window.resizable(width=FALSE, height=FALSE)
# End declaration Window

# Variables
index = 0
sorpresa = "Hello World John Master"
# End variables

#Functions 
def GetTextBtn(valor):
   global index
   screen.insert(index, valor)
   index +=1

def Delete(valor):
   screen.delete(0)

def Delete_all():
   screen.delete(0, END)

def Operations():
   eCuation = screen.get()
   getEcuation = eval(eCuation)
   screen.delete(0, END)
   screen.insert(0,getEcuation)
   index = 0

def sUrprise ():
   Click = screen.insert(index,sorpresa)

#End functions 

# Screen calculator
screen = Entry(window, font=("none 18"))
# End creen calculator

# Buttons calculator
button1 = Button(window, text="1", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(1))  
button2 = Button(window, text="2", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(2))  
button3 = Button(window, text="3", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(3))  
button4 = Button(window, text="4", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(4))  
button5 = Button(window, text="5", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(5))  
button6 = Button(window, text="6", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(6))  
button7 = Button(window, text="7", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(7))  
button8 = Button(window, text="8", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(8))  
button9 = Button(window, text="9", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(9))  
button0 = Button(window, text="0", bg="#334",fg="greenyellow", width=16, height=2, command= lambda: GetTextBtn(0)) 
# End buttons calculator

# Extra
surprise = Button(window, text = "Click Me! John Master", bg="darkblue", fg="#ff0",width=22, command = lambda: sUrprise())
# End extra

# Buttons aditional
button_reomve_all = Button(window, text="AC", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: Delete_all())
button_reomve_cU = Button(window, text="AC", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: Delete(0))               
button_equal = Button(window, text="=", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: Operations())                 
button_parentesisOpen = Button(window, text="(", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn('('))     
button_parentesisClose = Button(window, text=")", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn(')'))    
button_point = Button(window, text=".", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn('.'))              
# End buttons aditional

# Buttons algebry
button_split = Button(window, text="÷", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn('/'))          
button_multiply = Button(window, text="x", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn('*'))       
button_sum = Button(window, text="+", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn('+'))             
button_rest = Button(window, text="-", bg="#334",fg="greenyellow", width=6, height=2, command= lambda: GetTextBtn('-'))            
# End buttons algebry

# Screen position
screen.grid(padx=12, pady=12,columnspan=5)
# End screen position

# Buttons position
button1.grid(row=5, column=0, pady=3)
button2.grid(row=5, column=1, pady=3)
button3.grid(row=5, column=2, pady=3)
button4.grid(row=4, column=0, pady=3)
button5.grid(row=4, column=1, pady=3)
button6.grid(row=4, column=2, pady=3)
button7.grid(row=3, column=0, pady=3)
button8.grid(row=3, column=1, pady=3)
button9.grid(row=3, column=2, pady=3)
button0.grid(row=6, column=0, columnspan=2, pady=3)
# End buttons posiition

#Buttons aditional position
button_reomve_all.grid(row=1, column=3,pady=3)
button_reomve_cU.grid(row=2, column=2, pady=3)
button_equal.grid(row=6, column=3, pady=3)
button_parentesisOpen.grid(row=2, column=0, pady=3)
button_parentesisClose.grid(row=2, column=1, pady=3)
button_point.grid(row=6, column=2, pady=3)
#End buttons aditional position

# Buttons algebry position
button_split.grid(row=2, column=3, pady=3)
button_multiply.grid(row=3, column=3, pady=3)
button_sum.grid(row=4, column=3, pady=3)
button_rest.grid(row=5, column=3, pady=3)
# End buttons algebry position

# Surprise poisiton
surprise.grid(row=7, column=1, columnspan=2)
# End surprise poisiton
window.mainloop()
