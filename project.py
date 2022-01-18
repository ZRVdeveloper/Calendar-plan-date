from tkinter import *
import datetime
import year
import wekendDay
import workDay
from tkcalendar import Calendar

class KalendarDay():
	def __init__(self):
		pass

	def PlusSize(self,myLab):
		print (myLab)
		for my in myLab:
			myLab[my].config(font='Arial {}'.format(23))
	



if __name__ == '__main__':
    
    root = Tk()  
    wekend1 = []  
    work1 = []  
    root.geometry("400x400") 
    history = Label(text = "Кінець семестру {}".format(datetime.date.today()))    
    history.place(x = 10, y = 10)    
    wekendD = Label(text = "")    
    wekendD.place(x = 10, y = 30)
    workD = Label(text = "")    
    workD.place(x = 100, y = 30)
    main_manu = Menu()
    main_manu.add_command(label = 'Дата завершення навчання', command =lambda: year.YearBe(history))
    main_manu.add_command(label = 'Вихідні дні', command =lambda: wekendDay.wekend(wekendD,wekend1))
    main_manu.add_command(label = 'Робочі дні', command =lambda: workDay.workd(workD,work1))
    root.config(menu = main_manu)
    KalendarDay = KalendarDay()
    #Button(text = '1', command =lambda: print(wekend1)).pack()
    #Button(text = '2', command =lambda: print(work1)).pack()
    Button(text = 'Вирахувати', command =lambda: print('Рахумо')).place(x = 250, y = 10)
    Button(text = 'Зберегти', command =lambda: print('Збережено')).place(x = 250, y = 40)
    Button(text = 'Lher', command =lambda: print(wekendDay.wekend).place(x = 250, y = 40)
    lanOnRoot = [history, wekendD, workD]
    #Button(text = '+', command = lambda: KalendarDay.PlusSize(lanOnRoot)).pack()
    root.mainloop()