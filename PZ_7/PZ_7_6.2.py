# Дана строка-предложение на русском языке. Зашифровать ее, выполнив
# циклическую замену каждой буквы на следующую за ней в алфавите и сохранив при
# этом регистр букв («А» перейдет в «Б», «а» — в «б», «Б» — в «В», «я» — в «а» и т.
# д.). Букву «ё» в алфавите не учитывать («е» должна переходить в «ж»). Знаки
# препинания и пробелы не изменять.
sentence = "я люлю программирование "
result = ''
sentence = "я люблю пдф"
result = ''
for char in sentence:
    if char.isalpha():
        is_lower = char.islower()
        if char.lower() == 'е':
            result += 'ж' if is_lower else 'Ж'
        else:
            offset = 1
            encrypted_char = chr((ord(char) - ord('а') + offset) % 32 + ord('а')).upper() if not is_lower else chr((ord(char) - ord('а') + offset) % 32 + ord('а'))
            result += encrypted_char
    else:
        result += char

print("Исходное предложение:", sentence)
print("Зашифрованное предложение:", result)
