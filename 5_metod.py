city = 'Springfield'
list_1 = ['have', 'a', 'nice', 'day']
print(len(city))  # Вычисляет длину последовательности
print(city.find('g'))  # Поиск подстроки в строке. Возвращает индекс первого совпадения
print(city.index('g'))  # Поиск подстроки в строке. Возвращает индекс первого совпадения
print(city.count('i'))  # Подсчет количества вхождений подстроки в строку
print(city.replace('ing', 'e'))  # Заменить подстроку в строке на другую
print(city.split('i'))  # Разделяет строку по указанному разделителю
print(' '.join(list_1))  # Объединяет список строк list_1 в одну строку, используя разделитель ' '
print(city.upper())  # Преобразует все символы в строке к верхнему регистру

# 11
# 5
# 5
# 2
# Sprefield
# ['Spr', 'ngf', 'eld']
# have a nice day
# SPRINGFIELD