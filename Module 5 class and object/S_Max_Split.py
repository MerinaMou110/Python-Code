def call(s):
    store=[]
    count_s=0
    null_st=""
    for char in s:
        if char=='L':
            null_st+=char
            count_s+=1
           
        else :
            null_st+=char
            count_s-=1
            
        if count_s==0:
            store.append(null_st)
            null_st=""
    return store
  
str=input()
result=call(str)
print(len(result))
for result_str in result:
    print(result_str)


