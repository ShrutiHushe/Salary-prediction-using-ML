# Model use --> GUI

from tkinter import *
from tkinter.messagebox import *
from pickle import *
import os
import sys

def resource_path2(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception :
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

root = Tk()
root.title("Salary predictor by Shruti")
root.geometry("500x400+50+50")
root.configure(bg="lightblue")
f = ("Century", 30, "bold")

def predict():
	try:
		exp = float(ent_exp.get())
		f = open(resource_path2("sal.pkl"), "rb")
		model = load(f)
		f.close()
		sal = model.predict([[exp]])
		msg = "Salary = " + str(round(sal[0], 2)) + "K"
		showinfo("Msg ", msg)
	except ValueError:
		showerror("Issue", "u shud enter no's only")
		ent_exp.delete(0, END)
		ent_exp.focus()

lab_title = Label(root, text = "Salary Predictor", font=f)
lab_exp = Label(root, text = "Enter exp ", font=f)
ent_exp = Entry(root, font = f)
btn_predict = Button(root, text = "Predict salary", font=f,command=predict)

lab_title.pack(pady=5)
lab_exp.pack(pady=5)
ent_exp.pack(pady=5)
btn_predict.pack(pady=5)

root.mainloop()