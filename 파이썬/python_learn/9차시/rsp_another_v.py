import random
from tkinter import *
window = Tk()
Label(window, text='선택하세요',font=('Helvetica','16')).pack()
frame = Frame(window)

rock_image = PhotoImage(file='c:\\rock.png')
paper_image = PhotoImage(file='c:\\paper.png')
scissors_image = PhotoImage(file='c:\\scissors.png')

def pass_s():
    decide('scissors')
def pass_r():
    decide('rock')
def pass_p():
    decide('paper')

rock = Button(frame, image=rock_image, command=pass_r)
rock.pack(side='left')
paper = Button(frame, image=paper_image, command=pass_p)
paper.pack(side='left')
scissors = Button(frame, image=scissors_image, command=pass_s)
scissors.pack(side='left')

frame.pack()
Label(window, text='컴퓨터는 다음을 선택하였습니다.',font=('Helvetica','16')).pack()
computer_image = Label(window, image=rock_image)
computer_image.pack()
output = Label(window,text='',font=('Helvetica','16'))
output.pack()

def decide(user_choice):
    computer_choice = random.choice(['rock', 'scissors', 'paper'])
    if computer_choice == 'rock':
        computer_image['image'] = rock_image
    elif computer_choice == 'paper':
        computer_image['image'] = paper_image
    else:
        computer_image['image'] = scissors_image

    if user_choice == computer_choice:
        result = '비겼습니다.'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        result = '인간 승리!'
    else:
        result = '컴퓨터 승리!'
    output.config(text='인간 : '+user_choice +' 컴퓨터 : '+computer_choice+'  '+result)

window.mainloop()