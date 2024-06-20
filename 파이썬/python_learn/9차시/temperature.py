from tkinter import *

def process():
    tf = float(e1.get())
    tc = (tf-32.0)*5.0/9.0
    e2.delete(0,END)  #처음부터 끝까지 기존의 문자열 지우기
    e2.insert(0,str(tc))    #tc 변수의 값을 문자열로 변환하여 추가

def i_process():
    tc = float(e2.get())
    tf = tc*9.0/5.0+32
    e1.delete(0,END)
    e1.insert(0,str(tf))

window = Tk()

Label(window, text='화씨').grid(row=0, column=0)
Label(window, text='섭씨').grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window, text='화씨->섭씨',command=process).grid(row=2, column=1)
Button(window, text='섭씨->화씨',command=i_process).grid(row=2, column=2)
window.mainloop()