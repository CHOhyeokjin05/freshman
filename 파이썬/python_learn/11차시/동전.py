import random

pos = ['head','tail']
while True:
    sa = input('동전 던지기를 계속하시겠습니까?(yes/no) ')
    if sa == 'yes':
            computer = random.choice(pos)
            x = input('head or tail? ')
            if x == computer:
                print('성공')
            else:
                print('실패!')
                break
    elif sa == 'no':
        break
    else:
        print('잘못 입력했습니다.')


