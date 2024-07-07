# detail gulok hide kora hoy atai encapsulation
# encapsulation: hide details
# access modifier-->public,protected,privte

class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name      #public attribute
        self._bramch='moulovipara'        #protected. caile bahir theke access kora jay
        self.__balance=initial_deposit    #private attribute .class er baire access kora jabe nh

    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance=self.__balance-amount
            return amount
        else:
            return f'Your account have no balance'

mou=Bank('Merina',10000)
mou.holder_name='merina'
mou.deposit(40000)
print(mou.get_balance())    #output:50000
print(mou.holder_name)      
print(mou._bramch)     
print(mou._Bank__balance)   #private attribute avabe access kora jay

        
