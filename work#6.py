import re

while True:
    print('1 - Считать имена и фамилии:\n'
          '2 - Считать все емайлы:\n'
          '3 - Считать названия файлов:\n'
          '4 - Считать цвета:\n'
          '5 - Выход:\n')
    answer = int(input('Введите функцию: '))
    with open('MOCK_DATA.txt', 'r') as file:
        content = file.read()
    if answer == 1:
        names = re.findall(r"([A-Z][a-z]+)\s([A-Z][a-z]+|[A-Z]'[A-Z][a-z]+)", content)
        with open("names.txt", 'w') as file:
            for name, sur_name in names:
                file.write(f"{name} {sur_name}\n")
        print("Имена и фамилии записаны в файл names.txt.\n")
    elif answer == 2:
        emails = re.findall(r"[a-z0-9]+@[a-z0-9-]+\.[a-z0-9]+", content)
        with open("emails.txt", 'w') as file:
            for email in emails:
                file.write(f"{email}\n")
        print("Емейлы записаны в файл emails.txt.\n")
    elif answer == 3:
        file_names = re.findall(r"\s[A-Za-z]+\.[a-z0-9]+", content)
        with open("file_names.txt", 'w') as file:
            for file_name in file_names:
                file.write(f"{file_name.strip()}\n")
        print("Названия файлов записаны в файл file_names.txt.\n")
    elif answer == 4:
        colors = re.findall(r"#[0-9a-f]+", content)
        with open("colors.txt", 'w') as file:
            for color in colors:
                file.write(f"{color}\n")
        print("Цвета записаны в файл colors.txt.\n")
    elif answer == 5:
        print("Завершение!\n")
        break
    else:
        print("Произошла ошибка!\n")
