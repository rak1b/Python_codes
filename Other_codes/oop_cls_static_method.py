class student:
    minimum_age = 18
    total_student = 0
    def __init__(self,*args):
        self.name = args[0]
        self.age = args[1]
        self.country = args[2]
        student.total_student +=1

    def return_info(self):
        return f'Name : {self.name}\nAge : {self.age}\nCountry : {self.country}'
    @classmethod
    def minimum_age_changer(cls,age):
        print(cls)
        cls.minimum_age = age
    @classmethod
    def using_dash(cls,string):
        name,age,country = string.split('-')
        return cls(name,age,country)

    @staticmethod
    def weekend_checker(day):
        if day.lower() == "Friday".lower():
            return True
        else:
            return False

    def __add__(self, other):
        return int(self.age) + int(other.age)

    def __sub__(self, other):
        return int(self.age) - int(other.age)

    def __str__(self):
        return f'{self.name}-{self.age}-{self.country}'

    def __repr__(self):
        return f"student({self.name},{self.age},{self.country})"

rakib = student('Rakib',22,"bd")
rk = student.using_dash('Md Rakibul Islam-22-Bangladesh')
riddo = student.using_dash('Md Ranobi Islam-12-Bangladesh')
# print(student.total_student)
print(rk)
print(repr(rk))
# print(rakib+riddo)
# print(rakib-riddo)
