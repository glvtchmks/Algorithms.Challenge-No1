import os

input_file_path = input("Введіть шлях до вхідного файлу: ")

if not os.path.exists(input_file_path):
    print("Файл не знайдено!")
    exit()

output_file_path = input("Введіть шлях до вихідного файлу: ")

with open(input_file_path, "r", encoding="utf-8") as input_file:
    data = input_file.read()

    reversed_data = " ".join([word[::-1] for word in data.split()])

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(reversed_data)
        
    print("Дані успішно записані у файл.")