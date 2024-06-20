def addsub(x,y):
    return x+y,x-y
x,y = map(int,input('x,y 입력 : ').split())
print(f'합 : {addsub(x,y)[0]}, 차 : {addsub(x,y)[1]}')