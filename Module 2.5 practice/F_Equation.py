def equation(x,y):
    result=0
    for i in range(2,y+1,2):
        result+=x**i
    return result



x,y=map(int,input().split())
result=equation(x,y)
print(result)