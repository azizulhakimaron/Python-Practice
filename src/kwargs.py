#
def func(**kwarg):
    print (kwarg)
    print (type(kwarg))
def func1(n, **kwarg):
    for k,v in kwarg.items():
        print(f"{k}:{v}")
    print (n)
def func2(**kwarg):
    for k,v in kwarg.items():
        print(f"{k}:{v}")
    
d={"name":'aron',"age":24}
func(name='aron',age=24)
func1("luiccha",name='aron',age=24)
func2(**d)
#
def func3(name="Aron",age=24):
    print(name)
    print(age)
func3()
func3("Kasab",24)
