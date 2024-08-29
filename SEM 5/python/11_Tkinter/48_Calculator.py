from tkinter import *

window = Tk() 

window.title("Calculator")
window.geometry("500x300")

lb_num = Label(window, text = "Enter a Number")
lb_num.grid(row = 0,column = 0)

inp_num = Entry(window)
inp_num.grid(row = 0,column = 1)

lb_num2 = Label(window, text = "Enter a Number")
lb_num2.grid(row = 1,column = 0)

inp_num2 = Entry(window)
inp_num2.grid(row = 1,column = 1)



window.mainloop()