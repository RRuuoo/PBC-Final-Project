import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import datetime
# from PIL import ImageTk 

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
rgb7 = (231, 226, 71)		
bgcolor7 = '#%02x%02x%02x'% rgb7

s = input()  #開始時間
e = input()  #結束時間
start_time = datetime.datetime.strptime(s, "%H:%M")  #輸入半小時為單位(選單?)
end_time = datetime.datetime.strptime(e, "%H:%M")
delta = end_time - start_time
diff = delta/30  #時間差
timediff = str(diff).split(':')
contentlst = []  #景點list空集合
d = input()  #天數
for k in range(int(d)):
    contentlst.append([])
    n = input()  #組數
    for l in range(int(n)):
        content = input()  #格式：景點名,開始時間,待的時間(十分鐘為單位)
        lst = content.split(',')
        start = datetime.datetime.strptime(lst[1], "%H:%M")
        lst[1] = start
        contentlst[k].append(lst)
t = (start_time+datetime.timedelta(minutes=30))


class Schedule(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.create()
        
	def clickBtnMap(self):
		self.map = Toplevel()
		self.map.title('路線圖')

	def create(self):
		font1 = tkFont.Font(size = 12, family = "華康POP3體W12(P)")
		font2 = tkFont.Font(size = 12, family = "華康秀風體W3(P)")
		
		for i in range(int(timediff[1]) + 1):
			t = start_time+datetime.timedelta(minutes=30*i)
			self.lbl = tk.Label(self, text=t.strftime('%H:%M'), height=1, width=10,font=font1,bg=bgcolor2,fg="white")
			self.lbl.grid(row=i*3+1, column=0, sticky=tk.N)
		self.btnMap = tk.Button(self,text='路線圖',command=self.clickBtnMap,bg="green",fg="white",height=1,width=10,font=font1)
		self.btnMap.grid(row=int(timediff[1])*3 + 2, column=1)  
		self.date = tk.Label(self,text="星期列")
		self.date.grid(row=0,column=0)


		for j in range(int(d)):
			for m in range(len(contentlst[j])):
				self.blk = tk.Text(self, height=1, width=10, bg=bgcolor7,font=font2)
				a = contentlst[j][m][1] - start_time
				a1 = str(a).split(':')
				a1[1] = str(int(a1[1]) + int(a1[0])*60)
				b = contentlst[j][m][2]
				b1 = str(b).split(':')
				b1[1] = str(int(b1[1]) + int(b1[0])*60)
				self.blk.grid(row=int(int(a1[1])/10), column=j+1, rowspan=int(int(b1[1])/10), sticky = tk.SE + tk.NW)
				self.blk.insert('1.0', contentlst[j][m][0])
        


sch = Schedule()
sch.master.title('行程表')
sch.master.geometry('785x500')
sch.mainloop()