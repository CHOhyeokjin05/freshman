'''
from tkinter import *
cnt = 0
txt = '버튼 클릭 횟수 ' + str(cnt) + '회'.lstrip()
def process():
    global cnt
    cnt += 1
    txt = '버튼 클릭 횟수 ' + str(cnt) + '회'.lstrip()

window  = Tk()

button = Button(window,  text="증가!", command=process)
label = Label(text=txt)

button.pack()
label.pack()
window.mainloop()
'''

from tkinter import *

window  = Tk()
counter = 0

def clicked():
    global counter
    counter += 1
    label['text']  = '버튼클릭횟수: ' + str(counter)
def reset():
    global counter
    counter = 0
    label['text'] = '아직눌려지지않음'

label = Label(window,  text="아직눌려지지않음")
label.pack()
button = Button(window,  text="증가", command=clicked).pack()
r_button = Button(window, text='리셋', command=reset).pack()
window.mainloop()