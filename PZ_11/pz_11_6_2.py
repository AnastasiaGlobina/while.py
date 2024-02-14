#Из предложенного текстового файла (text18-6.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».
with open('text18-6.txt', 'r', encoding='utf-16') as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)
    spaces_count = content.count(' ')
    print("Количество пробельных символов:", spaces_count)

content_modified = content.replace('.', '!').replace(',', '!').replace(':', '!').replace(';', '!').replace('?','!').replace('!', '!').replace('-', '!')

with open('modified_text.txt', 'w', encoding='utf-8') as file:
    file.write(content_modified)

print("Текст успешно модифицирован и записан в файл 'modified_text.txt'.")