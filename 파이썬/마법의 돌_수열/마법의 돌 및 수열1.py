t=int(input())
print('')


def prt(i,j,t):
    for k in range(t-j):
        p=range(j+1,j+1+k+1)
        
        print(i,j,end=' ')
        print(*p)


for i in range(t,0,-1):
    print(i)
    if i<t:
        for j in range(t,i,-1):
            print(i,j)
            prt(i,j,t)
            
                


            
