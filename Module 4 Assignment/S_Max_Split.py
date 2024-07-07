s=input()
result=[]
empty_str=""
count=0
count1=0
for char in s:
    if char=='L':
        count=count+1
        empty_str+=char
    elif char=='R':
        count1+=1
        empty_str+=char
    if count==count1:
        result.append(empty_str)
        empty_str=""
        count=0
        count1=0
print(len(result))
for word in result:
    print(word)

