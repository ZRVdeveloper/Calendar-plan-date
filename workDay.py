import datetime
from tkinter import *
from tkcalendar import Calendar
class workd():
    def work(self, day):
            m = self.history.size()
            self.history.insert(m, day)
            self.history.pack(pady = 20)
    def returnWork(self):
        z = []
        m = ''
        self.history_place.config(text = "{}".format('-'))
        c = self.history.size()
        for i in range(c):
            op = self.history.get(i)
            self.workd.append(op)
        m = 'Робочі дні \n'    
        for d in range(len(self.workd)):
            m += self.workd[d] + '\n'  
        self.history_place.config(text='{}'.format(m))
        
        self.yearMain.destroy()

    def add_date(self):
        self.date.config(text = "Selected Date is: " + self.cal.get_date())
        self.Year = self.cal.selection_get()        
        self.work(self.Year)

    
    def create_year_main(self, today):
        #! Замість Tk() у багатовіконних програмах краще використовувати  Toplevel()
        self.yearMain = Toplevel()
        self.yearMain.geometry("250x800")
        Label(self.yearMain, text = 'Робочі дні', font = "Arial 24").pack()
        self.cal = Calendar(self.yearMain, selectmode = 'day',year = today.year, month = today.month,day = today.day, locale='uk')
        self.cal.pack(pady = 20)
        select = Button(self.yearMain, text = "Додати", command = self.add_date).pack(pady = 20)
        self.date = Label(self.yearMain, text = "")
        self.date.pack(pady = 20)  
        self.history = Listbox(self.yearMain)    
        self.history.pack(pady = 20)  
        self.add = Button(self.yearMain, text = "Встановити", command = self.returnWork).pack(pady = 20)
        self.date = Label(self.yearMain, text = "")
        #! А програме не маэ бути два mainloop(), ынфкше буде помилка     
        #self.yearMain.mainloop()


    def __str__(self):
        return "Nen dct ghj hjrb"
    def __init__(self,history_place,workd):
        self.today = datetime.date.today()
        self.history_place = history_place
        self.workd = workd
        self.Year = self.today
        self.create_year_main(self.today)
        

      

if __name__ == '__main__':  
    root = Tk()
    wekend1 = []    
    root.geometry("400x400") 
    history = Label(root) 
    todaybe = wekend(history, wekend1)
    m = todaybe.Year
    print (wekend1)
    root.mainloop()