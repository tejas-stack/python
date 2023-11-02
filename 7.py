def my_function():
    x=10
    print(x)
my_function()

def price():
    y=20
    x=10
    print(y,x)
price()



#global variable
x=25
def my_function():
    print(x)
my_function()

x=10
def modify_global():
    global xi
    x=20
    print(x)
modify_global()