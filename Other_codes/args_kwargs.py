def min_value(*value, **kvalue):
    def min_ret(*MIN_VAL):
        min = MIN_VAL[0]

        for i in MIN_VAL:
            if i < min:
                min = i

        return min

    def val_ret(*val):
        return min_ret(*val)

    def kval_ret(**kval):
        k = [k for k, v in kval.items()]
        return {min_ret(*k):kval[min_ret(*k)]}



    if len(value) > 0 and len(kvalue) > 0:
        return val_ret(*value),kval_ret(**kvalue)
    elif len(value) > 0 and len(kvalue) == 0:
        return val_ret(*value)
    elif len(value) == 0 and len(kvalue) > 0:
        return kval_ret(**kvalue)
    else:
        return "Please Pass Argument.."


ls = [10, 2, 34, 55, 6, 6]
dct = {
    'Rakib': 9,
    'Riddo': 10,
    'R':8,
    'Lowest':2,


}
print(min_value(**dct))
print(min_value(*ls))
print(min_value(*ls,**dct))
r = min_value(2,34,4,.5,5)
r = min_value(2,34,4,.5,5,*(1,23,4,55,6,0.22))
print(r)
