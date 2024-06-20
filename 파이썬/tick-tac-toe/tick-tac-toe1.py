board= [[' ' for x in range(3)] for y in range(3)]
start = True

def draw():
    for r in range(3):
        print(' '+board[r][0]+'| '+board[r][1]+'| '+board[r][2])
        if r!=2:
            print('--|--|--')

while start:
    if any(' ' in l for l in board):
        start = True
    else:
        start = False
    

    draw()
    



    
    x = int(input('x좌표 입력 (2차원 list 인덱스) : '))
    y = int(input('y좌표 입력 (2차원 list 인덱스) : '))

    if board[x][y] != ' ':
        print('잘못된 위치입니다.')
        continue
    else:
        board[x][y] = 'X'

    
    if board[1][1] != ' ' and board[2][2] == ' ':
        board[2][2] = 'O'
    else:
        if board[1][1] == ' ':
            board[1][1] = 'O'

        elif (board[0][0] == 'X' or board[2][0] == 'X') and board[0][2] == ' ' :
            board[0][2] = 'O'

        elif board[0][2] == 'X' and board[2][0] == ' ':
            board[2][0] = 'O'

        elif board[0][2] == 'O' and board[1][2] == ' ':
            board[1][2] = 'O'
            print('게임 오버')
            quit()
        
        elif board[2][0] == 'O' and board[2][1] == ' ':
            board[2][1] = 'O'
            print('게임 오버')
            quit()

        elif board[1][2] == 'X' and board[1][0] == ' ':
            board[1][0] = 'O'

        elif board[2][1] == 'X' and board[0][1] == ' ':
            board[0][1] = 'O'

        elif board[0][1] == 'X' and board[2][1] == ' ':
            board[2][1] = 'O'

        elif board[1][0] == 'X' and board[1][2] == ' ':
            board[1][2] = 'O'
        
        else:
            done = False
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ' and not done:
                        board[i][j] = 'O'
                        done = True
                        break;
    for p in range(3):
        if board[p][0]==board[p][1] and board[p][1]==board[p][2] and board[p][2] != ' ':
                print('게임 오버')
                quit()
        elif board[0][p]==board[1][p] and board[1][p]==board[2][p] and board[2][p] != ' ':
                print('게임 오버')
                quit()
        



    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        print('게임 오버')
        quit()
    elif board[2][0]==board[1][1] and board[1][1]==board[0][2]:
        print('게임 오버')
        quit()
    else:
        continue
        
        

        



'''



    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'; #세미콜론 붙여도 문법 오류 X
                done=True
                break;
                '''