class dog:
    def __init__(self,name):
        self.name=name
dog1=dog("buddy")
print(dog1.name)

class car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
car1=car("toyota","supra")
car2=car("maruti suziki","swift")
print(car1.model,car1.make)

x=input("enter the item number to get info:-")
class item:
    def __init__(self,item,price):
        self.item=item
        self.price=price
item1=item("french fries","150")
item2=item("sandwich","90")
item3=item("pasta","210")
item4=item("garlic bread","140")
item5=item("pizza","180")
print(x.item,x.price)

class bankaccount:
    def __init__(self,account_number,balance):
        self._account_number=account_number
        self._balance=balance
    def get_balance(self):
        return self._balance
account1=bankaccount("12345",1000)
print(account1._account_number)
print(account1.get_balance())