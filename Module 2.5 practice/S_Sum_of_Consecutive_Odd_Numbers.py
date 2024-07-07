t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    sum=0
    if x>y:
        temp=x
        x=y
        y=temp
    for i in range(x+1,y):
        if (i%2)!=0:
            sum=sum+i
    print(sum)
   
