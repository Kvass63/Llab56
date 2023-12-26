import numpy as np
import tkinter as tk
import os

def f1():
    global L
    n = 9
    L = np.empty((n, n), dtype=float)
    vvd = ''
    for i in range(n):
        for j in range(n):
            if i+j>2:
                L[i][j] = 2.7*i**2 + 3*i + j
            else:
                L[i][j] = np.sqrt(16.12*j + 0.8*i**2)
    for i in range(len(L)):
        for j in range(len(L)):
            vvd = vvd + str(round(L[i][j], 1)) + ' '
        vvd = vvd + '\n'
    txt1.configure(state=tk.NORMAL)
    txt1.delete('1.0', 'end')
    txt1.insert('1.0', vvd)
    txt1.tag_add('center', '1.0', 'end')
    txt1.configure(state=tk.DISABLED)
    btn2.configure(state=tk.NORMAL)
    f = open('ishodnaya.txt', 'w')
    f.write(vvd)
    f.close()
def f2():
    global L, srzn, X
    X = []
    vvd = ''
    vvd1 = ''
    srzn = np.average(L)
    L[0], L[4] = L[4], L[0]
    for i in range(len(L)):
        for j in range(len(L)):
            vvd = vvd + str(round(L[i][j], 1)) + ' '
        vvd = vvd + '\n'
    for i in range(len(L)):
        X.append(L[i][8-i])
        vvd1 = vvd1 + str(L[i][8-i]) + ' '

    txt2.configure(state=tk.NORMAL)
    txt2.delete('1.0', 'end')
    txt2.insert('1.0', vvd)
    txt2.tag_add('center', '1.0', 'end')
    txt2.configure(state=tk.DISABLED)
    ent3.configure(state=tk.NORMAL)
    ent3.delete('0', 'end')
    ent3.insert('0', vvd1)
    ent3.configure(state=tk.DISABLED)
    btn3.configure(state=tk.NORMAL)
    f=open('poluchm.txt', 'w')
    f.write(vvd)
    f.close()
    f=open('poluchv.txt', 'w')
    f.write(vvd1)
    f.close()
def f3():
    global X
    vvd = ''
    for i in range(len(X)-1):
        smallest = i
        for j in range(i+1, len(X)):
            if X[j] < X[smallest]:
                smallest = j
        X[i], X[smallest] = X[smallest], X[i]
    for i in range(len(X)):
        vvd = vvd + str(X[i]) + ' '
    ent3.configure(state=tk.NORMAL)
    ent3.delete('0', 'end')
    ent3.insert('0', vvd)
    ent3.configure(state=tk.DISABLED)
    f=open('peredvec.txt', 'w')
    f.write(vvd)
    f.close()
def f4():
    txt1.configure(state=tk.NORMAL)
    txt2.configure(state=tk.NORMAL)
    ent3.configure(state=tk.NORMAL)
    txt1.delete('1.0', 'end')
    txt2.delete('1.0', 'end')
    ent3.delete('0', 'end')
    btn2.configure(state=tk.DISABLED)
    btn3.configure(state=tk.DISABLED)
    os.remove('ishodnaya.txt')
    os.remove('poluchm.txt')
    os.remove('poluchv.txt')
    os.remove('peredvec.txt')

win = tk.Tk()
win.geometry('800x600')
win.title("Лаба 6")
win.config(bg='gray')

lb1 = tk.Label(win, text='Исходная матрица')
lb1.grid(row=1, column=1, pady=10)

txt1 = tk.Text(win,width=60 , height=10, state=tk.DISABLED)
txt1.tag_configure('center', justify='center')
txt1.grid(row=2, column=1, padx=10)

lb2 = tk.Label(win, text='Полученная матрица')
lb2.grid(row=3, column=1, padx=10, pady=10)

txt2 = tk.Text(win,width=60 , height=10, state=tk.DISABLED)
txt2.tag_configure('center', justify='center')
txt2.grid(row=4, column=1, padx=10)

lb3 = tk.Label(win, text='Полученный вектор')
lb3.grid(row=5, column=1, padx=10, pady=10)

ent3 = tk.Entry(win,width=60, state=tk.DISABLED)
ent3.grid(row=6, column=1, padx=10)

btn1 = tk.Button(win, text='Получить первую матрицу', command=f1)
btn1.grid(row=2, column=2, pady=10)

btn2 = tk.Button(win, text='Преобразовать матрицу и получить вектор', command=f2, state=tk.DISABLED)
btn2.grid(row=4, column=2, pady = 10)

btn3 = tk.Button(win, text='Преобразование вектора', command=f3, state=tk.DISABLED)
btn3.grid(row=6, column=2, pady=10)

btn4 = tk.Button(win, text='Очистить', command=f4)
btn4.grid(row=7, columnspan=2, column=1, pady = 10)
win.mainloop()