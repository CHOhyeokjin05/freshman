#4 3 3-4 2 2-4 2-3 2-3-4 1 1-4 ..... 적용
ttl,k,i=map(int,input().split())
a=[]
b=[]

print()
for i in range(ttl):
    a.append('i')

x=a[:]
b.append(x)


def prt(i,j):
        for x in range(4-j):
            print(i)
            print(j,'z')
            print('\n',x,'\n')
            print(x+4,'k')
        




for i in range(4,0,-1):
    print(i)
    for j in range(4,i,-1):
        print(i)
        print(j,'z')
        prt(i,j)