n=int(input())
array=list(map(int,input().split()))
max_a=array.index(max(array))
min_a=array.index(min(array))
array[max_a],array[min_a]=array[min_a],array[max_a]
print(*array)