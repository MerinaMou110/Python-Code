def full_name(first,last):
    name= f'full name is: {first} {last}'
    return name

# name=full_name('Alu', 'Kodu')
# print(name)
name=full_name(last='Alu', first='Kodu')
print(name)

#def famous(**kargs)                 ( key argument)
def famous_name(first,last,**addition):
    name=f'{first} {last}'
    # print(addition)
    # print(addition['title'])
    for key,value in addition.items():
        print(key, value)
    return name

name=famous_name(first='Taher' ,last='Ali',title='hujur',addition='Shayokh')
print(name)

# def function_name(num1,num2,*args, **kargs )

# return multiple things from an array
def a_lot(num1,num2):
    sum=num1+num2
    mult=num1*num2
    remain=num1-num2
    return [sum,mult,remain]

everything = a_lot(55,11)
print(everything)


def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")