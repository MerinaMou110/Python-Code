class shop:
    shopping_mall='jomuna'
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]    #cart is a instance attribute

    def add_to_cart(self,item):
        self.cart.append(item) 

mou=shop('merina mou')
mou.add_to_cart('shoes')
mou.add_to_cart('phone')
print(mou.cart)

auny=shop('Saiful Auny')
auny.add_to_cart('cap')
auny.add_to_cart('watch')
print(auny.cart)