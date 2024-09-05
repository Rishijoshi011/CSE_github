import tkinter as tk
from tkinter import PhotoImage 

window = tk.Tk()
window.title("Image")
window.geometry("1200x500")

image = PhotoImage(file="11_Tkinter/temp.png")

lb_name = tk.Label(window, image = image)
lb_name.pack()


window.mainloop()
