# list,array,collection is same(simple terms)

# index=  0  1  1  3  4  5  6  7  8  9
numbers=[45,56,12,89,87,32,89,59,46,93]
# index= -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(numbers[3],numbers[-3])  #output: 89 59

# list(start : end)   #start from the start index and stops before the end index
print(numbers[2:6])        #output: [12, 89, 87, 32]

#list(start : end : step)
print(numbers[1:7:1])   #output: [56, 12, 89, 87, 32, 89]
print(numbers[1:7:2])       #  [56, 89, 32]
print(numbers[7:2:-1])     #[59, 89, 32, 87, 89]
print(numbers[7:2:-2])    #[59, 32, 89]
print(numbers[4:])          #[87, 32, 89, 59, 46, 93]    index 4 theke shob print hbe


numbers =[7,8,5,4,3,2,4]
print(numbers[::-1])       #sesh theke shb print korbe