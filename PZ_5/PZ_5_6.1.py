#Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов.
def generate():
    while True:
      try:
        num_chars = int(input("Введите число символов: "))
        if num_chars < 0:
            print("Числот символов должно быть >  или = 0 ")
        else:
            output_string = 'A ' * num_chars
        print(output_string)
        break
      except ValueError:
        print ("Ошибка, введите целое число")
generate()