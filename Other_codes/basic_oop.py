class my_math:
    def __init__(self,a,b):
        self.value1 = a
        self.value2 = b

    def do_sum(self):
        return self.value1+self.value2

rk = my_math(1,2)
print(type(rk))

print(rk.do_sum())
new = my_math(3,4)
print(new.do_sum())
print(new)
