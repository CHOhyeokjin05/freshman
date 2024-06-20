import random
from tkinter import *

def vs(user_choice):
    computer_choice = random.choice(['rock', 'scissors', 'paper'])
    
    user_photo.config(image=photo_dict[user_choice])
    computer_photo.config(image=photo_dict[computer_choice])
    user_choice_label.config(text=f'사용자 선택: {user_choice}')
    computer_choice_label.config(text=f'컴퓨터 선택: {computer_choice}')

    if user_choice == computer_choice:
        result_label.config(text='비겼습니다.')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        result_label.config(text='이겼습니다.')
    else:
        result_label.config(text='졌습니다.')

window = Tk()

def rock_click():
    vs('rock')

def scissors_click():
    vs('scissors')

def paper_click():
    vs('paper')

photo_dict = {
    'rock': PhotoImage(file='C:/Users/Jin/Desktop/코딩/python_learn/9차시/rock.png'),
    'scissors': PhotoImage(file=r'C:\Users\Jin\Desktop\코딩\python_learn\9차시\scissors.png'),
    'paper': PhotoImage(file=r'C:\Users\Jin\Desktop\코딩\python_learn\9차시\paper.png')
}

rock_label = Label(window, image=photo_dict['rock'])
rock_label.grid(row=0, column=0)
rock_label.bind('<Button-1>', lambda event: rock_click())

scissors_label = Label(window, image=photo_dict['scissors'])
scissors_label.grid(row=0, column=1)
scissors_label.bind('<Button-1>', lambda event: scissors_click())

paper_label = Label(window, image=photo_dict['paper'])
paper_label.grid(row=0,column=2)
paper_label.bind('<Button-1>', lambda event: paper_click())

user_photo = Label(window)
user_photo.grid(row=1, column=0)

user_choice_label = Label(window, text='사용자 선택: 선택되지 않음')
user_choice_label.grid(row=2, column=0)

result_label = Label(window, text='', font=('Helvetica', 16))
result_label.grid(row=1, column=1)

computer_photo = Label(window)
computer_photo.grid(row=1, column=2)

computer_choice_label = Label(window, text='컴퓨터 선택: 선택되지 않음')
computer_choice_label.grid(row=2, column=2)



window.mainloop()
