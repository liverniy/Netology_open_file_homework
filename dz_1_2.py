import os


def recipes_reader(file_name: str, mode: str = 'r') -> dict:
    """Функция сбора словаря с рецептами из файла с рецептами"""
    cook_book_dic = dict()  # Проверяем наличие файла в директории
    if file_search(file_name):
        ingredients_list = []
        with open(file_name, mode) as recipes_file:  # Открываем файл с рецептами
            for line in recipes_file:
                if not line.strip() == '':  # Если строка не пустая
                    if not any(map(str.isdigit, line.strip())):  # Если строка не содержит цифр
                        dish_name = line.strip()  # Получаем название блюда
                    elif line.strip().isdigit():  # Если строка - число
                        quantity_of_ingredients = int(line.strip())
                    elif '|' in line.strip():  # Если строка содержит разделители, то это ингредиенты
                        ingredient_dic = dict()
                        line_split = line.strip().split('|')
                        if len(line_split) == 3:
                            ingredient_dic['ingredient_name'] = line_split[0].strip()
                            if line_split[1].isdigit:
                                ingredient_dic['quantity'] = int(line_split[1].strip())
                            ingredient_dic['measure'] = line_split[2].strip()
                        ingredients_list.append(ingredient_dic)
                        # Запись рецепта в словарь при проверке на количество входящих ингредиентов
                        if len(ingredients_list) == quantity_of_ingredients:
                            cook_book_dic[dish_name] = ingredients_list.copy()
                            ingredients_list.clear()
        return cook_book_dic


def file_search(file_name: str, folder_path=os.getcwd()) -> bool:
    """Функция наличия файла в папке с программой"""
    for element in os.scandir(folder_path):
        if element.is_file():
            if element.name == file_name:
                # print(f'File "{file_name}" found in folder {folder_path}')
                return True
    print(f'There is no file "{file_name}" in folder {folder_path}')
    return False


def get_shopping_list_by_dishes(dishes: list, person_count: int):
    cook_book = recipes_reader('recipes.txt')
    shopping_list = dict()
    for dish in dishes:
        if dish in cook_book:
            # print(cook_book[dish])
            # ingredients_list += cook_book[dish]
            for ingredient in cook_book[dish]:
                # abc = {ingredient['ingredient_name']:
                #            {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}}
                ingredient_name = ingredient['ingredient_name']

                if ingredient_name in shopping_list.keys():
                    if shopping_list[ingredient_name]['measure'] == ingredient['measure']:
                        shopping_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
                    else:
                        print(f'У продукта {ingredient_name} в рецептах {", ".join(dishes)} разные размерности.\n'
                              f'Необходимо привести рецепты к единой размерности, чтобы составить список покупок')
                        return False
                else:
                    shopping_list[ingredient_name] = \
                        {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                # print(shopping_list[ingredient['ingredient_name']])
        else:
            print(f'{dish} - незнакомый рецепт')
    return shopping_list


def netology_dz_1_and_2():
    cook_book = recipes_reader('recipes.txt')
    print()
    print(cook_book)
    print()

    shopping_list1 = get_shopping_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    shopping_list2 = get_shopping_list_by_dishes(['Тако с говядиной', 'Фахитос'], 2)

    print(shopping_list1)
    print()
    print(shopping_list2)


netology_dz_1_and_2()
