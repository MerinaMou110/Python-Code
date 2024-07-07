class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]

    def add_to_cart(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)
    
    def checkout(self,amount):
        total=0
        for item in self.cart:
            # print(item)
            total+=item['price']*item['quantity']
        print('total price',total)
        if amount<total :
            print (f'please provide {total-amount} more') 
        else:
             extra=amount-total
             print(f'Here is your item and extra money {extra}')
   
    def remove_item(self,item):
        for product in self.cart:
            if product['item']==item:
                self.cart.remove(product)
 
mou=Shopping('Merina Mou')
mou.add_to_cart('alu',50,6)
mou.add_to_cart('dim',12,24)
mou.add_to_cart('rice',50,5)
print(mou.cart)
mou.checkout(900)
mou.remove_item('rice')
print(mou.cart)










