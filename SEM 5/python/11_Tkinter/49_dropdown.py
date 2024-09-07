import tkinter as tk

window = tk.Tk()

window.geometry("500x300")
window.title("Dropdown menu")

def dp():
    label.config(text=clicked.get())  
    
options = ["Los Santos", "San Ferro", "Las Ventures", "Chicago", "Liberty"]

clicked = tk.StringVar()

clicked.set("San Ferro")

drop = tk.OptionMenu(window, clicked, *options)
drop.grid(row = 0, column = 0)

button = tk.Button(window, text = "click here", command = dp)
button.grid(row = 1, column = 0)

label = tk.Label(window, text = "")
label.grid(row = 2, column = 0)

window.mainloop()
