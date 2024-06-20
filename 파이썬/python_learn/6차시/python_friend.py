menu = 0
name = []
while menu != 9:
    print('------------------')
    print('1. 친구 리스트 출력')
    print('2. 친구추가')
    print('3. 친구삭제')
    print('4. 이름변경')
    print('9. 종료')
    menu = int(input('메뉴를 선택하시오 : '))
    
    if menu == 1:
        print(name)
    elif menu == 2:
        n = input('이름을 입력하시오 : ')
        name.append(n)
    elif menu == 3:
        try:
            n = input('삭제하고 싶은 이름을 입력하시오 : ')
            name.remove(n)
        except:
            print('잘못된 이름입니다.')
    elif menu == 4:
        n = input('변경하고 싶은 이름을 입력하시오 : ')
        if n in name:
            index = name.index(n)
            new_n = input('새 이름을 입력하시오 : ')
            name[index] = new_n
        else:
            print('잘못된 이름입니다.')