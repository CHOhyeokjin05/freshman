import random

count = 0

for i in range(100):
    seed_money = 50

    while seed_money <250:

        if seed_money <=0:
            break

        x = random.randint(0,1)

        if x == 1:
            seed_money += 1
        else:
            seed_money -= 1

    if seed_money == 250:
        count += 1
    else:
        continue

print('초기 금액 : $50')
print('목표 금액 : $250')
print(f'100번 중에서 {count}번 성공')
