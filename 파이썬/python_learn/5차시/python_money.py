def weeklyPay(rate, hour):
    if hour > 30:
        return rate*hour*1.5
    else:
        return rate*hour
    
rate = int(input('시급 입력 : '))
hour = int(input('근무 시간 입력 : '))
total = weeklyPay(rate, hour)
print(f'주급은 {total}입니다.')