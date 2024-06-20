t=int(input())
print('')


def recursive(j):
    step=j
    if step==t:
        print('')
        return
    else:
        for i in range(t-j):
            print(step+1,end=' ')
            recursive(j+1)
        

#3,4   2,3,4 이런 부분을 재귀적으로 해결하고 싶음.
for i in range(t,0,-1):
    print(i)
    if i<t:
        for j in range(t,i,-1):
            print(i,j,end=' ')
            recursive(j)