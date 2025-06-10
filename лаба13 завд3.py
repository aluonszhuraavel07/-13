import tkinter as tk
import math

def calculate_sum():
    try:
        x = float(entry_x.get())
        total = 0
        for k in range(1, 8):
            numerator = k * math.cos(x + k)
            denominator = math.log(2 + x) + 2 * k
            total += numerator / denominator

        result_var.set(f"Сума = {total:.4f}")
    except:
        result_var.set("Помилка у введенні!")

root = tk.Tk()
root.title("Проєкт 'Сума'")

tk.Label(root, text="Введіть x:").grid(row=0, column=0)
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1)

tk.Button(root, text="Обчислити", command=calculate_sum).grid(row=1, column=0, columnspan=2)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).grid(row=2, column=0, columnspan=2)

root.mainloop()
