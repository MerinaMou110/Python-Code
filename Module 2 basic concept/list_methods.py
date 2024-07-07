numbers = [12,45,98,68]
numbers.append(56)
print(numbers)

numbers.insert(0,71)
numbers.insert(2,81)
print(numbers)

if 98 in numbers:
    numbers.remove(98)
if 8 in numbers:
    numbers.remove(45)
print(numbers)

last=numbers.pop()
print(last,numbers)

if 5 in numbers:
    index=numbers.index(5)
    print(index)

index=numbers.index(71)   #koto number index a ase bolbe
print(index)

sorted=numbers.sort()
print(numbers)

numbers =[22,19,19,14,33]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)



