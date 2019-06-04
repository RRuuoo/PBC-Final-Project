import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

class Window(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self, width=30, height=20, bg='white')
		self.grid()
		self.create_widgets()
	def create_widgets(self):
		font2 = tkFont.Font(size = 16, family = "華康POP3體W12(P)")
		self.image = tk.PhotoImage(file = "C:\\Users\\yanig\\Downloads\\台南走透透.png")
		self.label1 = tk.Label(self, image = self.image, height=300, width=785)
		self.label1.grid(row=0, column=0,pady=15)
		# self.btn1 = tk.Button(self, height=1, width=15, bg="red", text="Let's Go！", font=font2, fg="white")
		# self.btn1.grid(row=10, column=2, columnspan=20, rowspan=1)

		
mywindow = Window()
mywindow.master.title("Welcome Page")
mywindow.master.geometry('785x400')
mywindow.master.configure(background='white')
btn1 = tk.Button(mywindow.master,height=1,width=15,bg="red",text="Let's Go！",font=("華康POP3體W12(P)",20),fg="white")
btn1.place(x=250, y=350)
mywindow.mainloop()