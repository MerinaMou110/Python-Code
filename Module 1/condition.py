a=7
boss=True

if a>5:
    print('5 er besi')
    print('something')
elif a>3:
    print('olpo boro') 
elif a==2:  
    print('ekdom dui er soman soman')      

else:
    print('5 er kom')  


# if boss is True:   
#     print('come in')
# else:
#     print('get out')       

if boss is not True:
    print('get out')
else:
    print('come in kuddus')    


coin='head'
# nested conditions
if boss==True:
    print('boss you are good')
    if coin=='tail':
        print('batting')
    else:
        print('bowling')
        if 5>2 or boss!=True:
            print('do something')
            if 8%2==0 and 5%2==1:
                print('8 is an even number')

else:
    print('you are not my boss')
