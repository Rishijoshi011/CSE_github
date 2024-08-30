import tkinter as tk

window = tk.Tk()
window.title("Registration Form")
window.geometry("500x300")

lb_name = tk.Label(window, text = "Username")
lb_name.grid(row = 0, column = 0, padx = 10, pady = 5)

inp_name = tk.Entry(window)
inp_name.grid(row = 0, column = 1, padx = 10, pady = 5)

lb_pass = tk.Label(window, text = "Password")
lb_pass.grid(row = 1, column = 0, padx = 10, pady = 5)

inp_pass = tk.Entry(window, show = "*")
inp_pass.grid(row = 1, column = 1, padx = 10, pady = 5)

lb_email = tk.Label(window, text = "Email")
lb_email.grid(row = 2, column = 0, padx = 10, pady = 5)

inp_email = tk.Entry(window)
inp_email.grid(row = 2, column = 1, padx = 10, pady = 5)

lb_result = tk.Label(window, text="")
lb_result.grid(row = 4, column = 1, pady = 5)

lb_gender = tk.Label(window, text="Gender")
lb_gender.grid(row = 3, column = 0, padx = 10, pady = 5)

gender_var = tk.StringVar(value = "Male")

male = tk.Radiobutton(window, text="Male", variable = gender_var, value = "Male")
male.grid(row = 3, column = 1, padx = 10, pady = 5)

female = tk.Radiobutton(window, text="Female", variable = gender_var, value = "Female")
female.grid(row = 3, column = 2, padx = 10, pady = 5)

btn_login = tk.Button(window, text="Register")
btn_login.grid(row = 4, column = 1, pady = 10)

window.mainloop()
