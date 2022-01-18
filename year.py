import datetime
from tkinter import *
from tkcalendar import Calendar
class YearBe():
    
    def work(self):
            self.history.config(text = "Кінець семестру {}".format(self.Year))
            self.history.place() 
            self.d = 1

    def grad_date(self):
        self.date.config(text = "Selected Date is: " + self.cal.get_date())
        self.Year = self.cal.selection_get()
        self.yearMain.destroy()
        self.work()

    
    def create_year_main(self, today):
        #! Замість Tk() у багатовіконних програмах краще використовувати  Toplevel()
        self.yearMain = Toplevel()
        self.yearMain.geometry("400x400")
        Label(self.yearMain, text = 'Закінчення семестру', font = "Arial 24").pack()
        self.cal = Calendar(self.yearMain, selectmode = 'day',year = today.year, month = today.month,day = today.day, locale='uk')
        self.cal.pack(pady = 5)
        Button(self.yearMain, text = "Встановити", command = self.grad_date).pack(pady = 5)
        self.date = Label(self.yearMain, text = "")
        self.date.pack(pady = 5)   
        #! А програме не маэ бути два mainloop(), ынфкше буде помилка     
        #self.yearMain.mainloop()


    def __str__(self):
        return "Nen dct ghj hjrb"
    def __init__(self,history):
        self.d = 0
        self.today = today = datetime.date.today()
        self.history = history
        self.history.config(text = "Кінець семестру {}".format('-'))
        self.Year = self.today
        self.create_year_main(self.today)
        

      

if __name__ == '__main__':    
    todaybe = YearBe(today)
    m = todaybe.Year
    print (m)