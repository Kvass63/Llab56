import tkinter as tk
from PIL import Image, ImageTk

A = [[2.5, 3.7], [-4.6, 0.4]]
B = [[2.3, 7.8, 9.1], [-6.7, 1.2, 2.1], [-15.9, 0.6, 0.5]]
C = [[4.8, 0.8], [-3.6, 0.1]]

def summatr(x):
    s = 0
    for i in range(len(x)):
        for j in range(len(x[0])):
            s += x[i][j]
    return round(s, 1)

def f():
    global A, B, C
    vvd = ''
    x1 = summatr(A)
    x2 = summatr(B)
    x3 = summatr(C)

    X = [x1, x2, x3]
    for i in X:
        vvd = vvd + str(i) + ' '
    ent.delete(0, 'end')
    ent.configure(state=tk.NORMAL)
    ent.insert('0', vvd)
    ent.configure(state=tk.DISABLED)

win = tk.Tk()
win.geometry('1070x600')
win.config(bg='gray')
win.title('Лаб 5')

zg = tk.Label(win, text='Лабораторная работа №5', font=('Arial Black', 17))
zg.grid(row=1, columnspan=2, column=1, pady=20, padx=20)

lb1 = tk.Label(win, text='Исходные данные:', font=('Arial', 14))
lb1.grid(row=2, column=1, padx=10)

canvas = tk.Canvas(win, width=1025, height=346)
image = Image.open('image_2023-11-24_15-53-09.png')
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid(row=3, column=1, pady=20, padx=20)

ent = tk.Entry(win, width=20, font=('Arial', 14), state=tk.DISABLED)
ent.grid(row=4, column=1, padx=20)

btn = tk.Button(win, text='Вычислить!', command=f)
btn.grid(row=5, column=1, pady=20, padx=20)

win.mainloop()