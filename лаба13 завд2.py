import tkinter as tk
import math

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Півпериметр
        p = (a + b + c) / 2

        # Висота до сторони c
        h_c = (2 / a) * math.sqrt(p * (p - a) * (p - b) * (p - c))

        # Бісектриса до сторони a
        w_a = (2 * b * c * math.cos(math.acos((b**2 + c**2 - a**2) / (2 * b * c)) / 2)) / (b + c)

        result_label.config(text=f"Висота h_c = {h_c:.2f}\nБісектриса w_a = {w_a:.2f}")
    except:
        result_label.config(text="Помилка у вхідних даних!")

root = tk.Tk()
root.title("Проєкт 'Трикутник'")

tk.Label(root, text="Сторона a:").place(x=10, y=10)
entry_a = tk.Entry(root)
entry_a.place(x=100, y=10)

tk.Label(root, text="Сторона b:").place(x=10, y=40)
entry_b = tk.Entry(root)
entry_b.place(x=100, y=40)

tk.Label(root, text="Сторона c:").place(x=10, y=70)
entry_c = tk.Entry(root)
entry_c.place(x=100, y=70)

tk.Button(root, text="Обчислити", command=calculate).place(x=100, y=100)

result_label = tk.Label(root, text="")
result_label.place(x=10, y=140)

root.geometry("300x200")
root.mainloop()
