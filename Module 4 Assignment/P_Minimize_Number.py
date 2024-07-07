
def all_even(array):
    for a in array:
        if a%2!=0:
            return False
    return True

n=int(input())
array=list(map(int,input().split()))
count=0
count_a=0
while all_even(array):
    array = [num // 2 for num in array]
    count+=1
print(count)
