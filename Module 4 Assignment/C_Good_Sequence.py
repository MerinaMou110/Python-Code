

# N = int(input())
# a = list(map(int, input().split()))

# if not a:
#     print()
# else:
   
#     count = [0] * (max(a) + 2)  
#     remove_count = 0

   
#     for num in a:
#         count[num] += 1

    
#     for i in range(1, max(a) + 1):
#         if count[i] > i:
#             remove_count += count[i] - i
#         elif count[i] < i:
#             remove_count += count[i]

    
#     print(remove_count)



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