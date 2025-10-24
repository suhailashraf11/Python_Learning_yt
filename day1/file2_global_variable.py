# this is all about learning global variable


# 1. Variable that  are created outside  of the fucntion. Can be used everywhere , both inside of fucntions outside of fucntions

x = 'awesome'
def  myfun():
    print('python is ' + x)
myfun()





# the global keyword

# 1. To create a global variable inside a function, you can use the global keyword.
def  myfunc():
    global  x
    x = 'Fantastic'
myfunc()
print("Python is " + x)



# also can be used keyword if you want to change global variable  inside a fucntion
x = 'awesome'
def myfunc():
    global x
    x = "fantastic "
myfunc()
print("Python is " + x)
