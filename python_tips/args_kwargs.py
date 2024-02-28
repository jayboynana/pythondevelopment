a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9]
print(*a)
def show1(name,*args):
    print(name)
    print(args)
    print(type(args))

show1('a',a,b)

def show2(name,**kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

show2('b',key1='value1',key2='value2')