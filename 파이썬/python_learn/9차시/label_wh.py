from tkinter import *
window  = Tk()

Label(window,  text="너비").grid(row=0)
Label(window,  text="높이").grid(row=1)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

photo = PhotoImage(file="C:/Users/Jin/Pictures/Screenshots/스크린샷 2024-04-29 144913.png")

label = Label(window,  image=photo)
label.grid(row=0,  column=2, columnspan=2, rowspan=2)

Button(window, text='이미지저장').grid(row=2, column=0, columnspan=2)

# 두번째버튼과세번째버튼은2열과3열에표시한다.
Button(window, text='확대').grid(row=2,  column=2)
Button(window, text='축소').grid(row=2,  column=3)

window.mainloop()