import time
import random

x = [6,5,3,1,8,7,2]
y = []

start = time.time()

#삽입정렬 => 메모리를 더 잡아먹는 because 추가 리스트 존재.
y.append(x[0])
for i in range(1,len(x)):
    for j in range(len(y)):
        if x[i]>y[j]:
            continue
        else:
            y.insert(j,x[i])
            break
    if j == len(y)-1:   #j가 len(y)-1 에서 아예 멈춤.
        y.append(x[i])


end = time.time()

print(y)
print(end-start)


#병합 정렬
y=[]

def merge(x):

    #재귀 => 리스트 분할
    if len(x) < 2:
        return x
    
    mid = len(x)//2
    low_x = merge(x[:mid])
    high_x = merge(x[mid:])

    merged_x = []
    l = h = 0
    while l<len(low_x) and h<len(high_x):
        if low_x[l] < high_x[h]:
            merged_x.append(low_x[l])
            l+=1
        else:
            merged_x.append(high_x[h])
            h+=1
    merged_x += low_x[l:]
    merged_x += high_x[h:]
    return merged_x




y=merge(x)
print(y)