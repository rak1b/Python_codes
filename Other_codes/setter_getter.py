class person:
    def __init__(self,first_name:str,last_name:str):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def email(self):
        return f'{self.first_name}_{self.last_name}@email.com'


    @email.setter
    def email(self,email):
        fullname,email_com = email.split('@')
        first_name,last_name = fullname.split('_')
        self.first_name = first_name
        self.last_name = last_name
    @email.deleter
    def email(self):
        self.first_name =None
        self.last_name =None

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

ob1 = person('Rakibul','Islam')

print(ob1)
ob1.email = 'MdRakibul_Islam@email.com'
del ob1.email
print(ob1.email)

