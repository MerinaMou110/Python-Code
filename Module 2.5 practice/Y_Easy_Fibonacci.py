def fibo(n):
    fibo_s=[0,1]
    if n==0:
        return 0
    for i in range(2,n):
        next_fibo=fibo_s[-1]+fibo_s[-2]
        fibo_s.append(next_fibo)
    return fibo_s[0:n]
N=int(input())
result=fibo(N)
print(*result)