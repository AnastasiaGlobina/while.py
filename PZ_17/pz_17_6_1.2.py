import tkinter as tk

def print_digits():
    try:
        number = int(entry_number.get())
        if number <= 0:
            label_result.config(text="Введите положительное целое число")
            return
        result_text = ""
        number_str = str(number)[::-1]  # Convert to string and reverse
        for digit in number_str:
            result_text += f"{digit}\n"
        label_result.config(text=result_text)
    except ValueError:
        label_result.config(text="Вы ввели не число, попытайтесь ввести цифры!")

root = tk.Tk()
root.title("Print Digits")

label_number = tk.Label(root, text="Введите целое число:")
label_number.pack()
entry_number = tk.Entry(root)
entry_number.pack()

button = tk.Button(root, text="Напечатать цифры", command=print_digits)
button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()