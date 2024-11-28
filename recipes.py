def read_recipes_from_file(filepath):
  """
  Читает рецепты из файла и возвращает словарь рецептов.

  Args:
    filepath: Путь к файлу с рецептами.

  Returns:
    Словарь рецептов, где ключи - названия блюд, а значения - списки словарей
    с ингредиентами (название, количество, единица измерения). Возвращает None,
    если файл не найден.
  """
  try:
    with open(filepath, 'r', encoding='utf-8') as f:
      cook_book = {}
      while True:
        dish_name = f.readline().strip()
        if not dish_name:
          break # Конец файла

        ingredients_count = int(f.readline().strip())
        ingredients = []
        for _ in range(ingredients_count):
          line = f.readline().strip().split(' | ')
          ingredients.append({
            'ingredient_name': line[0],
            'quantity': int(line[1]),
            'measure': line[2]
          })
        cook_book[dish_name] = ingredients
      return cook_book
  except FileNotFoundError:
    print(f"Ошибка: файл {filepath} не найден.")
    return None


def main():
  filepath = 'r'C:\Users\hp\Desktop\recipes\recipes.txt # Обратите внимание на r перед строкой
  cook_book = read_recipes_from_file(filepath)
  if cook_book:
    print(cook_book)

if __name__ == "__main__":
  main()