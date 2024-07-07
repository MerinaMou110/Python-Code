x,y=map(int,input().split())
array=list(map(int,input().split()))

for _ in range(y):
    m,n=map(int,input().split())
    k=m-1
    sum=0
    for j in range(k,n):
     sum=sum+array[j]
  
    print(sum)

