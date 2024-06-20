board= [[' ' for x in range(3)] for y in range(3)]
cnt = 0
hist = []


def memory(x,y):
    hist.append((x,y))
    if len(hist) == 3:
        del hist[0]


def line(x,y):
    done = False

    try:

        if hist[0][0] == hist[1][0]:
            for i in range(3):
                if board[x][i] == ' ' and not done:
                    board[x][i] = 'O'
                    done = True
                    return done
        elif hist[0][1] == hist[1][1]:
            for i in range(3):
                if board[i][y] == ' ' and not done:
                    board[i][y] = 'O'
                    done = True
                    return done
    except:
        pass
            


def c_think(x,y):
    done = False
    if board[1][1] == ' ':
        board[1][1] = 'O'

    elif board[1][1] == 'O':



        done = line(x,y)

        if done != True:

            if board[0][0] == ' ':
                board[0][0] = 'O'
            elif board[2][0] == ' ':
                board[2][0] = 'O'
            elif board[0][2] == ' ':
                board[0][2] = 'O'
            elif board[2][2] == ' ':
                board[2][2] = 'O'
            else:

                done = False
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == ' ' and not done:
                            board[i][j] = 'O'
                            done = True
                            break

    else:
        done = line(x,y)

        if done != True:

            if board[0][0] == ' ':
                board[0][0] = 'O'
            elif board[2][0] == ' ':
                board[2][0] = 'O'
            elif board[0][2] == ' ':
                board[0][2] = 'O'
            elif board[2][2] == ' ':
                board[2][2] = 'O'
            else:

                done = False
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == ' ' and not done:
                            board[i][j] = 'O'
                            done = True
                            break




def draw():
    for r in range(3):
        print(' '+board[r][0]+'| '+board[r][1]+'| '+board[r][2])
        if r!=2:
            print('--|--|--')

while True:

    draw()
    
    x = int(input('x좌표 입력 (2차원 list 인덱스) : '))
    y = int(input('y좌표 입력 (2차원 list 인덱스) : '))
    
    if board[x][y] != ' ':
        print('잘못된 위치입니다.')
        continue
    else:
        board[x][y] = 'X'
        cnt += 1

    memory(x,y)
    c_think(x,y)
    cnt += 1


    for p in range(3):
        if board[p][0]==board[p][1] and board[p][1]==board[p][2] and board[p][0] != ' ':
                print('\n게임 오버')
                draw()
                quit()
        elif board[0][p]==board[1][p] and board[1][p]==board[2][p] and board[0][p] != ' ':
                print('\n게임 오버')
                draw()
                quit()
        

    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and cnt > 4:
        print('\n게임 오버')
        draw()
        quit()

    elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and cnt > 4:
        print('\n게임 오버')
        draw()
        quit()

    else:
        continue
        
        

        



