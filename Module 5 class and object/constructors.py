class Phone:
    manufactured='china'

    def __init__(self,owner,brand,price):  #constructor
        self.owner = owner
        self.brand=brand
        self.price=price

    def send_sms(self,phone,sms):
        text=f'sending to:{phone} {sms}'
        print(text)

# create object with different instance attribute
my_phone=Phone('kala chan','oppo',9800)
print(my_phone.owner,my_phone.brand,my_phone.price)

her_phone=Phone('my phone','i phone',120000)
print(her_phone.owner,her_phone.brand,her_phone.price)
