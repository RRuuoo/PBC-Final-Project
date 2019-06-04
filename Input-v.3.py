import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

#調色盤
rgb1 = (92, 128, 188) #rgb顏色設定
bgcolor1 = '#%02x%02x%02x'% rgb1 #將rgb格式轉成hex格式
rgb2 = (46, 196, 182)		
bgcolor2 = '#%02x%02x%02x'% rgb2
rgb3 = (216, 247, 147)		
bgcolor3 = '#%02x%02x%02x'% rgb3
rgb4 = (253, 255, 252)		
bgcolor4 = '#%02x%02x%02x'% rgb4
rgb5 = (249, 87, 56)		
bgcolor5 = '#%02x%02x%02x'% rgb5
rgb6 = (255, 159, 28)		
bgcolor6 = '#%02x%02x%02x'% rgb6


class Window(tk.Frame):
	
	def __init__(self):
		tk.Frame.__init__(self, width=30, height=20, bg=bgcolor3)
		self.grid()
		self.create_widgets()
	
	def create_widgets(self):
		
		#字型設定
		font1 = tkFont.Font(size = 32, family = "華康POP3體W12(P)")
		font2 = tkFont.Font(size = 16, family = "華康POP3體W12(P)")
		font3 = tkFont.Font(size = 12, family = "Noto Sans TC Black")
		
		#Build Object/建立物件
		self.lb1 = tk.Label(self, height=1, width=30, bg=bgcolor3, text="台南走透透", font = font1, fg = bgcolor1)

		self.lb2 = tk.Label(self, height=1, width=10, bg=bgcolor2, text="選擇遊玩天數", font = font2, fg = bgcolor4)
		self.sv = StringVar()
		self.sv.set("Choose")
		self.om = tk.OptionMenu(self, self.sv, "一日","二日","三日","四日","五日")
		self.om.config(width=9,font = font3)
		
		self.lb3 = tk.Label(self, height=1, width=10, bg=bgcolor6, text="出發時間", font = font2, fg = bgcolor4)
		self.txt1 = tk.Text(self, height=1, width=15, font = font3)
		
		self.lb4 = tk.Label(self, height=1, width=10, bg=bgcolor5, text="結束時間", font = font2, fg = bgcolor4)
		self.txt2 = tk.Text(self, height=1, width=15, font = font3)
		
		self.lb5 = tk.Label(self, height=1, width=10, bg=bgcolor2, text="想去的景點", font = font2, fg = bgcolor4)
		self.txt3 = tk.Text(self, height=1, width=15, font = font3)
		
		self.lb6 = tk.Label(self, height=1, width=10, bg=bgcolor6, text="出發地點", font = font2, fg = bgcolor4)
		self.txt4 = tk.Text(self, height=1, width=15, font = font3)
		
		self.lb7 = tk.Label(self, height=1, width=10, bg=bgcolor5, text="住宿地點", font = font2, fg = bgcolor4)
		self.txt5 = tk.Text(self, height=1, width=15, font = font3)

		self.but1 = tk.Button(self,height=1, width=15, bg=bgcolor2, text="排程", font = font2, fg = bgcolor4)
		
		#Assign Position/指定位置
		self.lb1.grid(row=0, column=0, columnspan=20, rowspan=2,pady=15)
		
		self.lb2.grid(row=3, column=1, columnspan=4, rowspan=1, pady=15)
		self.om.grid(row=3, column=4, columnspan=5, rowspan=1, pady=15)
		
		self.lb3.grid(row=5, column=1, columnspan=4, rowspan=1, pady=15)
		self.txt1.grid(row=5, column=4, columnspan=5, rowspan=1, pady=15)
		
		self.lb4.grid(row=7, column=1, columnspan=4, rowspan=1, pady=15)
		self.txt2.grid(row=7, column=4, columnspan=5, rowspan=1, pady=15)
		
		self.lb5.grid(row=9, column=1, columnspan=4, rowspan=1, pady=15)
		self.txt3.grid(row=9, column=4, columnspan=5, rowspan=1, pady=15)

		self.lb6.grid(row=5, column=10, columnspan=4, rowspan=1, pady=15)
		self.txt4.grid(row=5, column=13, columnspan=5, rowspan=1, pady=15)

		self.lb7.grid(row=7, column=10, columnspan=4, rowspan=1, pady=15)
		self.txt5.grid(row=7, column=13, columnspan=5, rowspan=1, pady=15)

		self.but1.grid(row=9, column=12, columnspan=4, rowspan=1, pady=15)

mywindow = Window()
mywindow.master.title("輸入資訊")
mywindow.master.geometry('785x400')
mywindow.master.configure(background=bgcolor3)
mywindow.mainloop()