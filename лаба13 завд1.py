import tkinter as tk
import math

# Вхідні дані
a = 5
b = 2
c = 5.4

# Обчислення значення функції
numerator = c ** math.e - 4 * math.log10(a) - (b * c % 1)
denominator = math.log(b)
f = numerator / denominator

# Створення вікна
root = tk.Tk()
root.title("Обчислення функції f")

# Створення міток і полів з результатом
tk.Label(root, text="Значення змінних:").grid(row=0, column=0, sticky='w')
tk.Label(root, text=f"a = {a}").grid(row=1, column=0, sticky='w')
tk.Label(root, text=f"b = {b}").grid(row=2, column=0, sticky='w')
tk.Label(root, text=f"c = {c}").grid(row=3, column=0, sticky='w')

tk.Label(root, text="Результат f:").grid(row=4, column=0, sticky='w')
tk.Label(root, text=f"{f:.4f}").grid(row=4, column=1, sticky='w')

# Запуск вікна
root.mainloop()