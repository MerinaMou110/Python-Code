from menu import Pizza,Burger,Drinks,Menu
from restaurant import Restaurant
from User import Chef,Customer,Server,Manager
from order import Order
def main():
    menu=Menu()
    pizza_1=Pizza('cheese pizza',800,'large',['cheese','meat','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2=Pizza('Normal pizza',300,'large',['onion','meyonese','potato'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3=Pizza('vegetables pizza',400,'large',['capsicum','oil','onion'])
    menu.add_menu_item('pizza',pizza_3)

    # add burger to the menu
    burger_1=Burger('Naga Burger',1000,'chicken',['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2=Burger('Beef Burger',1200,'beef',['meat','cheese'])
    menu.add_menu_item('burger',burger_2)

    #add drinks to the menu
    coke=Drinks('Coke',50,True)
    menu.add_menu_item('drinks',coke)
    coffee=Drinks('Mocha',300,False)
    menu.add_menu_item('drinks',coffee)

    # show Menu
    menu.show_menu()
    restaurant=Restaurant('Sai baba restaurant',2000,menu)
     
    # add employees
    manager=Manager('MerinaMou',5,'merinamou@gmail.com','moulovipara',1500,'jan 1 2020','core')
    restaurant.add_employee('manager',manager)
    chef=Chef('Rustom baburchi',6,'chupa@rustam.com','rustomnagar',3500, 'Feb 1,2020','Chef','everything')
    restaurant.add_employee('chef',chef)
    server=Server('Choto server',6,'nai@jai.com','restaurant',200,'March 1,2020','server')
    restaurant.add_employee('server',server)


   # show employee
    restaurant.show_employees()

    #customer 1 placing an order
    customer_1=Customer('sakib khan',6,'kink@khan.com','banani',100000)
    order_1=Order(customer_1,[pizza_3,coke,burger_1,pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    # customer one paying for order_1
    restaurant.receive_payment(order_1,20000,customer_1)

    print('revenue and balance after first customer', restaurant.revenue,restaurant.balance)

    #customer 2 placing an order
    customer_2=Customer('munir khan',6,'kink@khan.com','banani',100000)
    order_2=Order(customer_2,[pizza_1,burger_2,burger_1,pizza_2,coffee])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

    # customer one paying for order_2
    restaurant.receive_payment(order_2,5000,customer_1)
    print('revenue and balance after second customer', restaurant.revenue,restaurant.balance)


    #pay rent
    restaurant.pay_expense(restaurant.rent,'Rent')
    print('after rent',restaurant.revenue,restaurant.balance,restaurant.expense)

    restaurant.pay_salary(chef)
    print('after salary', restaurant.revenue,restaurant.balance,restaurant.expense)

#call the main
if __name__=='__main__':
    main()