#static attribute(class attribute)
#static method @staticmethod
#class method  @classmethod
#difference between static method and class method

class Shopping:
    cart=[]  #class  attribute #static attribute
    origin='china'
    
    def __init__(self,name,location) -> None:
        self.name='jamu na city'  #instance attribute
        self.location='jam er majhkhane'


    def purchase(self,item,price,amount):
        remaining=amount-price
        print(f'buying: {item} for price: {price} and remaining : {remaining}')
    
    @staticmethod     #staticmethod use korle self dite hobe nh
    def multiply(a,b):
        result=a*b
        print(result)

    @classmethod       #classmethod use korle sorasori class dia access korleo self equal to kisui dite hoy nh
    def hudai_dekhi(self,item):
        print('i want to be a free bird',item)

basundhara=Shopping('basundhara', 'not popular location')
# basundhara.purchase('lungi',500,1000)
# Shopping.purchase('a',2,3,3)
# basundhara.hudai_dekhi('Coxs bazar')
Shopping.hudai_dekhi('Coxs bazar')

#static method
Shopping.multiply(4,6)     #instance sara
basundhara.multiply(4,6)  