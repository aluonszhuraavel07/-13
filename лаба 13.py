from tkinter import *
from random import *
from tkinter import messagebox

a = []
def mas():
    n = edit1.get()
    if not n:
        messagebox.showerror('Помилка', 'Розмірність масиву не вказана')
        return

    n = int(n)
    a.clear()
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    for i in range(n):
        a.append(randint(-50, 50))
        listbox1.insert(END, a[i])

#  Сортування за спаданням методом обміну
def sort():
    n = len(a)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    listbox2.delete(0, END)
    for i in range(n):
        listbox2.insert(END, a[i])

#  Обчислення суми
def compute_sum():
    s = sum(a)
    label4['text'] = 'sum = ' + str(s)

#  Подвоїти всі кратні 4
def double_multiples_of_four():
    for i in range(len(a)):
        if a[i] % 4 == 0:
            a[i] *= 2
    listbox1.delete(0, END)
    for value in a:
        listbox1.insert(END, value)

#  Про автора
def about_author():
    messagebox.showinfo('Про автора', 'Автор: Журавель Альона\nEmail: zuravelalona3@gmail.com')

#  Умова задачі
def problem_statement():
    messagebox.showinfo('Умова задачі',
        'Збільшити вдвічі всі елементи одновимірного масиву, кратні 4.\n'
        'Після цього виконати сортування за спаданням методом обміну.')

#  Теми оформлення
def set_light_theme():
    root['bg'] = 'lightgray'
    listbox1['bg'] = 'white'
    listbox2['bg'] = 'white'
    for label in (label1, label2, label3, label4):
        label['bg'] = 'lightgray'
        label['fg'] = 'black'
    edit1['bg'] = 'white'

def set_dark_theme():
    root['bg'] = 'black'
    listbox1['bg'] = 'gray80'
    listbox2['bg'] = 'gray80'
    for label in (label1, label2, label3, label4):
        label['bg'] = 'black'
        label['fg'] = 'white'
    edit1['bg'] = 'gray80'

def set_default_theme():
    root['bg'] = '#F0F0F0'
    listbox1['bg'] = '#FFFFFF'
    listbox2['bg'] = '#FFFFFF'
    for label in (label1, label2, label3, label4):
        label['bg'] = '#F0F0F0'
        label['fg'] = 'black'
    edit1['bg'] = '#FFFFFF'

#  Контекстне меню
x = y = 0
def do_popup(event):
    global x, y
    x = event.x
    y = event.y
    popupmenu.post(event.x_root, event.y_root)  

root = Tk()
root.title('Масиви')
root.geometry('600x350')

label1 = Label(text='Вихідний масив')
label2 = Label(text='Посортований масив')
label1.place(x=20, y=30)
label2.place(x=200, y=30)

listbox1 = Listbox(height=10, width=20)
listbox2 = Listbox(height=10, width=20)
listbox1.place(x=20, y=70)
listbox2.place(x=200, y=70)

label3 = Label(text='Кількість елементів масиву:')
label3.place(x=400, y=30)

edit1 = Entry()
edit1.place(x=400, y=70)

button1 = Button(text='Заповнити', width=20, command=mas)
button1.place(x=400, y=100)

button2 = Button(text='Сортувати', width=20, command=sort)
button2.place(x=400, y=130)

button3 = Button(text='Обчислити суму', width=20, command=compute_sum)
button3.place(x=400, y=160)

button4 = Button(text='Подвоїти кратні 4', width=20, command=double_multiples_of_four)
button4.place(x=400, y=190)

label4 = Label(text='sum =')
label4.place(x=400, y=230)

# Головне меню
main_menu = Menu(root)
root.config(menu=main_menu)

array_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Дії з масивом', menu=array_menu)
array_menu.add_command(label='Заповнити', command=mas)
array_menu.add_command(label='Сортувати', command=sort)
array_menu.add_command(label='Обчислити суму', command=compute_sum)
array_menu.add_command(label='Подвоїти кратні 4', command=double_multiples_of_four)

about_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Про програму', menu=about_menu)
about_menu.add_command(label='Про автора', command=about_author)
about_menu.add_command(label='Умова задачі', command=problem_statement)

popupmenu = Menu(root, tearoff=0)
popupmenu.add_command(label="Світлий", command=set_light_theme)
popupmenu.add_command(label="Темний", command=set_dark_theme)
popupmenu.add_command(label="Відновити початкові кольори", command=set_default_theme)
root.bind("<Button-3>", do_popup)

root.mainloop()
