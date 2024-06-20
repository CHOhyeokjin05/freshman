cnt = 0
while True:
    temp = int(input('소요시간을 입력하세요(종료하려면 -1 입력) : '))
    if temp>=5 and temp <= 15:
        print('[0] {0}번째 손님 매칭 (수요시간 : {1}분)'.format(cnt,temp))
        cnt += 1
    elif temp == -1:
        print('프로그램을 종료합니다.')
        break
    else:
        print('[ ] {0}번째 손님 매칭 안됨 (소요시간 : {1})'.format(cnt,temp))
print('총 탑승 승객 : {0}명'.format(cnt))