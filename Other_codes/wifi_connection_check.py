from datetime import datetime,date,time,timedelta

class wifi_user:
    def __init__(self,username,user_id,speed,password,month_date,start_date,payment=None):
        self.username = username
        self.user_id = user_id
        self.speed = speed
        self.__password = password
        self.month_date = month_date
        self.start_date =start_date
        self.__payment = payment
    def give_payment(self):
    def connection_check(self):
        pass

    def set_start_date(self,year,month,date):
        self.start_date = datetime(year,month,date).date()
    def show_pass(self):
        return self.__password

    def change_pass(self,new_pass):
        self.__password = new_pass

    def __str__(self):
        return f"Username:{self.username}\nMonthly payment data:{self.month_date}\nWifi speed:{self.speed}"



Rakib = wifi_user('Rak1b','123445','4mbps','Rakibrk11','20','20-8-20')


Rakib.set_start_date(2020,9,21)
start_datee = Rakib.start_date
one_month =timedelta(days=30)
last_date = start_datee + one_month
print(last_date)
