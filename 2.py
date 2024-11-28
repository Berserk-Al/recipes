def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """
  Генерирует список покупок для указанных блюд и количества персон.

  Args:
      dishes: Список названий блюд.
      person_count: Количество персон.
      cook_book: Словарь рецептов.

  Returns:
      Словарь с названием ингредиентов и их количеством для всех блюд.
      Возвращает None, если хотя бы одно блюдо отсутствует в cook_book.
  """
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f"Ошибка: блюдо '{dish}' не найдено в кулинарной книге.")
            return None
        for ingredient in cook_book[dish]:
            new_quantity = ingredient['quantity'] * person_count
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': new_quantity
                }
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += new_quantity
    return shop_list


# Пример использования:
cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
    ]
}

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
if shop_list:
    print(shop_list)

