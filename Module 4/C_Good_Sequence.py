N = int(input())
a = list(map(int, input().split()))

mp={}
for num in a:
    if num in mp:
        mp[num]+=1
    else:
        mp[num]=1
sum_r=0
for key,value in mp.items():
    if key>value:
        sum_r+=value
    elif key<value:
        sum_r+=(value-key)
print(sum_r)

