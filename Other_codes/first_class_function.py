def max(list):
    max = list[0]
    for i in list:
        if i>max:
            max = i
    return max
ls = [90.1,100,143]

# def return__max(func,list):
#     return func(list)
#
# rs = return__max(max,ls)
# print(rs)
# a = max
# print(a(ls))
#
# def return__min()

# def print_msg():
#     def help_print(msg):
#         print(msg)
#     return help_print
#
# lets_print = print_msg()
# print(lets_print)
# print(lets_print('Rakib'))


def f_func(rk):
    def c_func():
        print(rk)
        def another_func():
           print(rk)
        return another_func()
    return c_func()

print(f_func('Md Rakibul islam'))
