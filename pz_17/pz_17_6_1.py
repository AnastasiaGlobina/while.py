import tkinter as tk

def calculate_sum():
    number = int(entry_number.get())
    numbers = int(entry_numbers.get())
    sum = 0
    if number < numbers:
        for i in range(number, numbers + 1):
            sum += i
        label_result.config(text=f"Сумма чисел от {number} до {numbers} равна: {sum}")
    else:
        label_result.config(text=f"{number} больше {numbers}")

root = tk.Tk()
root.title("Sum of Numbers")

label_number = tk.Label(root, text="Введите первое число:")
label_number.pack()
entry_number = tk.Entry(root)
entry_number.pack()

label_numbers = tk.Label(root, text="Введите второе число:")
label_numbers.pack()
entry_numbers = tk.Entry(root)
entry_numbers.pack()

button = tk.Button(root, text="Расчитать сумму", command=calculate_sum)
button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
