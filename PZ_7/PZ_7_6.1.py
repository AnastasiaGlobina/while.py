#Дан символ C, изображающий цифру или букву (латинскую или русскую). Если C
#изображает цифру, то вывести строку «digit», если латинскую букву — вывести
#строку «lat», если русскую — вывести строку «rus».
def check_char_type(char):
    if char.isdigit():
        return "digit"
    elif char.isalpha():
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            return "lat"
        else:
            return "rus"
    else:
        return "Не буквы и не цифры"
char= '12'
result = check_char_type(char)
print("Результат: ", result)