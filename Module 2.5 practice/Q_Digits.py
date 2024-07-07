# T=int(input())
# n=0
# while n<T:
#     num=int(input())
#     while num>0:
#      r=num%10
#      v=num//10
#      print(r,end=" ")    
#      num=v
#     n=n+1
#     print()


T = int(input())
for _ in range(T):
    N = int(input())
    digits = []

    while N > 0:
        digits.append(N % 10)
        N //= 10

    print(*digits[::])


