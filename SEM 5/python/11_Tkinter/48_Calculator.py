import tkinter as tk

def addition():
    result = int(inp_num.get()) + int(inp_num2.get())
    lb_result.config(text=f"Result: {result}")

def subtraction():
    result = int(inp_num.get()) - int(inp_num2.get())
    lb_result.config(text=f"Result: {result}")

def multiplication():
    result = int(inp_num.get()) * int(inp_num2.get())
    lb_result.config(text=f"Result: {result}")

def division():
    try:
        result = int(inp_num.get()) / int(inp_num2.get())
        lb_result.config(text=f"Result: {result:.2f}")
    except ZeroDivisionError:
        lb_result.config(text="Error: Division by Zero")

window = tk.Tk() 

window.title("Calculator")
window.geometry("500x300")

lb_num = tk.Label(window, text = "Enter a Number")
lb_num.grid(row = 0,column = 0)

inp_num = tk.Entry(window)
inp_num.grid(row = 0,column = 1)

lb_num2 = tk.Label(window, text = "Enter a Number")
lb_num2.grid(row = 1,column = 0, pady= (10, 5))

inp_num2 = tk.Entry(window)
inp_num2.grid(row = 1,column = 1)

btn_plus = tk.Button(window, text = "+", width = "9", command = addition)
btn_plus.grid(row = 2,column = 0, pady= (10, 5))

btn_min = tk.Button(window, text = "-", width = "9", command = subtraction)
btn_min.grid(row = 2,column = 1)

btn_mul = tk.Button(window, text = "*", width = "9", command = multiplication)
btn_mul.grid(row = 3,column = 0, pady= (10, 5))

btn_div = tk.Button(window, text = "/", width = "9", command = division)
btn_div.grid(row = 3,column = 1)

lb_result = tk.Label(window, text = "Result:")
lb_result.grid(row = 4, column = 0, columnspan=2, pady= (10, 5))

window.mainloop()
