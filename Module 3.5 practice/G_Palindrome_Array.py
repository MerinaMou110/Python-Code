t=int(input())

array=list(map(int,input().split()))
if(array==array[::-1]):
    print('YES')
else:
    print('NO')