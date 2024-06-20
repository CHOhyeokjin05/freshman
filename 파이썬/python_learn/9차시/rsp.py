import random
from tkinter import *

def vs():
    computer = random.choice(['rock', 'scissors','paper'])

    user = input('rock, scissors, paper 중 하나 입력 : ')

    if user == computer:
        print('비겼습니다.')

    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        print('이겼습니다.')

    else:
        print('졌습니다.')

window = Tk()


photo_rock = PhotoImage(file = 'rock.png')
photo_scissors = PhotoImage(file = 'scissors.png')
photo_paper = PhotoImage(file = 'paper.png')


