# global variable
balance=3000

def buy_things(item,price):
    # local scope variable
    # you can access the global variable without using global keyword
    # if you want to modify a global variable ,you have to use the global keyword
    global balance
    balance=balance-price
    print(f'balance after buying {item}',balance)


buy_things('sunglass',1000)