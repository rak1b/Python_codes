def details_adder(name_fun):
    def say_name():
        name ="Md Rakibul Islam"
        print(name)
        return name_fun()
    return say_name
@details_adder
def say_age():
    age = 12
    print(age)
say_age()

@details_adder
def say_country():
    country='Bd'
    print(country)

say_country()
# v = details_adder(say_name)
# v()
