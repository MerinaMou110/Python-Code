class Phone:
    price=19000
    color='blue'
    brand='samsung'
    features=['camera','speaker','hammer']

    def call(self):
        print('calling one person')
    def send_sms(self,phone,sms):     #parameter hishabe first a self dita hobe. first take ignore korbe
        text=f'sending SMS to: {phone} and messege: {sms}'
        return text

my_phone=Phone()
print(my_phone.features)
my_phone.call()
result=my_phone.send_sms(4127,'I missed you')
print(result)

