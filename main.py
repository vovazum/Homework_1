import os # импортируем библиотеку

#  Ппрочитаем файл recipes.txt
path = os.path.join(os.getcwd(), 'recipes.txt')
with open(path, encoding='utf-8') as cook_file: # добавляем кодировку utf-8 для удобного чтения
    cookbook = {}  # Создаем пустой словарь для поваренной книги
    for string in cook_file:
        dish = string.strip()  # Выбираем из файла название блюда
        ingredients_count = int(cook_file.readline().strip())  # Выбираем из файла количество ингредиентов для блюда
        dish_dict = []  # Создаем пустой список для словарей с блюдами поваренной книги
        for item in range(ingredients_count):
            #  Выбираем из файла ингредиенты по разделителю '|'
            ingredient_name, quantity, measure = cook_file.readline().strip().split('|')
            #  Добавляем в список словари с ингредиентами
            dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cookbook[dish] = dish_dict  #  Добавляем в поваренную книгу блюда и их ингредиенты
        cook_file.readline()  # Пропускаем пустую строку

print('Задача №1: Получили словарь\n================================')
print(cookbook)



#  Создаем функцию для получения списка покупок исходя из заказанных блюд и количества персон
def get_shop_list_by_dishes(dishes, person_count):
    grocery_dict = {}  # Создаем пустой словарь для хранения списка покупок
    for dishs in dishes:
        for ingredient in cookbook[dishs]:  # Выбираем ингредиенты для блюд из поваренной книги
            #  Добавляем ингредиеты, увеличивая их количество на число персон
            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            #  Проверяем заказанное блюдо на предмет повтора, если блюдо уже есть в списке, то увеличиваем количество
            #  Иначе добавляем ингредиент в список покупок
            if grocery_dict.get(ingredient['ingredient_name']) == 'None':
                _merger = (int(grocery_dict[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                grocery_dict[ingredient['ingredient_name']]['quantity'] = _merger
            else:
                grocery_dict.update(ingredient_list)
    return grocery_dict


print('\nЗадача №2: Получить словарь с названием ингредиентов и его количества для блюда.\n================================')
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))




# Получаем список файлов в папке их пути sorted
folder_path = 'sorted'
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Создаем словарь для хранения данных
file_contents = {}

# Читаем содержимое файлов и подсчитываем количество строк
for file_name in file_names:
    with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents[file_name] = {
            'num_lines': len(lines),
            'content': lines
        }

# Сортируем словарь по количеству строк в файле
sorted_contents = sorted(file_contents.items(), key=lambda x: x[1]['num_lines'])

# Записываем отсортированное содержимое в файл
with open(os.path.join(folder_path, 'result.txt'), 'w', encoding='utf-8') as result_file:
    for file_name, content in sorted_contents:
        result_file.write(f'{file_name}\n{content["num_lines"]}\n')
        result_file.writelines(content['content'])


print('\nЗадача №3: Необходимо объединить их в один по следующим правилам \n1. Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них. \n2. Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем. \n================================')
print('Готово! Результат записан в файл result.txt в папке sorted')



