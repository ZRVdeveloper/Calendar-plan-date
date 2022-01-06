from tkinter import *
import datetime
from tkcalendar import Calendar

class YearBe():
	def work(self):
			self.history.config(text = self.Year)
			history.pack(pady = 20)
	def grad_date(self):
		self.date.config(text = "Selected Date is: " + self.cal.get_date())
		self.Year = self.cal.selection_get()
		self.yearMain.destroy()
		self.work()
		print (self.Year)

    
	def create_year_main(self, today):
    	#! Замість Tk() у багатовіконних програмах краще використовувати  Toplevel()
		self.yearMain = Toplevel()
		self.yearMain.geometry("400x400")
		self.cal = Calendar(self.yearMain, selectmode = 'day',year = today.year, month = today.month,day = today.day, locale='uk')
		self.cal.pack(pady = 20)
		Button(self.yearMain, text = "Get Date", command = self.grad_date).pack(pady = 20)
		self.date = Label(self.yearMain, text = "")
		self.date.pack(pady = 20)   
		#! А програме не маэ бути два mainloop(), ынфкше буде помилка     
		#self.yearMain.mainloop()


	def __str__(self):
		return "Nen dct ghj hjrb"
	def __init__(self,today,history):
		self.today = today
		self.history = history
		self.Year = self.today
		self.create_year_main(self.today)
		

  


	



if __name__ == '__main__':
    
    root = Tk()
    today = datetime.date.today()
    root.geometry("400x400")    
    history = Label(text = "43")
    history.pack(pady = 20)
    main_manu = Menu()
    main_manu.add_command(label = 'Встановити рік', command =lambda: YearBe(today,history))
    root.config(menu = main_manu)
    root.mainloop()