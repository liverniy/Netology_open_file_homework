import os


def file_search(file_name: str, folder_path=os.getcwd()) -> bool:
    """Функция наличия файла в папке с программой"""
    for element in os.scandir(folder_path):
        if element.is_file():
            if element.name == file_name:
                # print(f'File "{file_name}" found in folder {folder_path}')
                return True
    # print(f'There is no file "{file_name}" in folder {folder_path}')
    return False


def count_line_in_file(file_name: str):
    """Функция определения количества строк в файле"""
    with open(file_name) as file:
        return sum(line.count('\n') for line in file)


def add_new_clear_file(new_file_path, file_name):
    """
    Функция создания нового пустого файла с заданным именем в указанной директории
    или отчистки существующего файла с указанным именем
    """
    result_file_path = os.path.join(new_file_path, file_name)
    open(result_file_path, 'w').close()
    return result_file_path


def netology_dz3():
    """Основной блок программы"""
    base_path = os.getcwd()
    sub_path = os.path.join(base_path, 'sorted')
    file_dict = dict()
    for file_name in ['1.txt', '2.txt', '3.txt']:
        file_path = os.path.join(sub_path, file_name)
        if file_search(file_name, sub_path):  # Проверка наличия файла с данным именем в папке
            file_dict[file_name] = count_line_in_file(file_path)  # Заполняем словарь {'имя файла': кол-во строк}
    # Создаем итоговый файл и получаем путь к нему
    result_file_path = add_new_clear_file(sub_path, 'result.txt')
    # Заполняем файл с учетом задания
    for counter in sorted(file_dict.values()):  # Получаем количество строк в отсортированном по длине файла словаре
        for file_name, count_line in file_dict.items():
            source_file_path = os.path.join(sub_path, file_name)
            if count_line == counter:
                with open(source_file_path) as source_file, open(result_file_path, 'a') as result_txt:
                    result_txt.write(file_name + '\n')
                    result_txt.write(str(count_line) + '\n')
                    for line in source_file:
                        result_txt.write(line.strip() + '\n')


netology_dz3()
