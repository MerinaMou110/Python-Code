numbers = [45,87,65,43,85,14,26,61]

odds=[]
for num in numbers:
    if num%2==1 and num%5==0:
        odds.append(num)

print(odds)                             #output: [45, 65, 85]
odd_nums= [num for num in numbers]      ##output: [45, 87, 65, 43, 85, 14, 26, 61] 

# odd_nums= [num for num in numbers if num%2==1]     #[45, 87, 65, 43, 85, 61]
odd_nums= [num for num in numbers if num%2==1 if num%5==0]  
print(odd_nums)      

players=['sakib','musfik','mustafiz']
ages=[38,34,32]

age_comb=[]
for player in players:
    print('player:',player)                 
    for age in ages:
        print(player,age)
        age_comb.append([player,age])
print(age_comb)

# aivabeo kora jay
age_comb2=[[player,age]for player in players for age in ages]
print(age_comb2)


# output:
# player: sakib
# sakib 38
# sakib 38
# sakib 32
# player: musfik
# musfik 38
# musfik 38
# musfik 32
# player: mustafiz
# mustafiz 38
# mustafiz 38
# mustafiz 32
# [['sakib', 38], ['sakib', 38], ['sakib', 32], ['musfik', 38], ['musfik', 38],
#  ['musfik', 32], ['mustafiz', 38], ['mustafiz', 38], ['mustafiz', 32]] 


