import datetime
from tkinter import *
from tkcalendar import Calendar

class Year():
    def grad_date(self):
        self.date.config(text = "Selected Date is: " + self.cal.get_date())
        self.Year = self.cal.selection_get()
        print (self.Year)

    
    def create_year_main(self, today):
        self.yearMain = Toplevel()
        self.yearMain.geometry("400x400")
        self.cal = Calendar(self.yearMain, selectmode = 'day',year = today.year, month = today.month,day = today.day, locale='uk')
        self.cal.pack(pady = 20)
        Button(self.yearMain, text = "Get Date", command = self.grad_date).pack(pady = 20)
        Button(self.yearMain, text = "Get Date", command = self.yearMain.destroy).pack(pady = 20)
        self.date = Label(self.yearMain, text = "")
        self.date.pack(pady = 20)


    def __str__(self):
        return "Nen dct ghj hjrb"
        
    def __init__(self,today):
        self.today = today 
        self.Year = self.today
        self.create_year_main(self.today)

        self.yearMain.mainloop()

        

if __name__ == '__main__':
    
    today = datetime.date.today()
    todaybe = Year(today)
    m = todaybe.Year
    print (m)