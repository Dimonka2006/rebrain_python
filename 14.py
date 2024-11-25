# Дан список словарей, отображающих количество общей и занятой памяти на накопителях:

resource = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]
# Создайте скрипт, который:

# Запрашивает у пользователя номер накопителя, который нужно проверить.

while True:
    user_input = input("Введите номер накопителя, который нужно проверить: ")
    disk_number = int(user_input) - 1 # счет начинается с 0
    if disk_number >= len(resource) or disk_number < 0:
        print(f"введите число от 1 до {len(resource)}: ") 
    break

# Вычисляет количество и процент свободной памяти на выбранном накопителе.

def get_disk_info(disk_number):
    total_memory = resource[disk_number]['total']/1024**3   # переводим байты в ГБ
    used_memory = resource[disk_number]['used']/1024**3  # переводим байты в ГБ
    
    free_memory = int(total_memory - used_memory)
    free_percent = round((free_memory / total_memory) * 100, 1)
    
    return {
        'free_memory': free_memory,
        'free_percent': free_percent
    }
info = get_disk_info(disk_number)
# print(info)
# Выдает пользователю сообщение:
# 3.1. Если свободной памяти осталось меньше 10Гб или меньше 5%, то выводится сообщение:

# 'на накопителе <номер накопителя> критически мало свободного места'

if info['free_memory'] < 10 or info['free_percent'] < 5:
    print(f"На накопителе {disk_number + 1} критически мало свободного места!")


# 3.2. Если свободной памяти больше, чем в предыдущем пункте, но меньше 30Гб или меньше 10%, то выводится сообщение:

# 'на накопителе <номер накопителя> мало свободного места'
elif info['free_memory'] < 30 or info['free_percent'] < 10:
    print(f"На накопителе {disk_number + 1} мало свободного места.")

# 3.3. Иначе выводится сообщение:

# 'на накопителе <номер накопителя> достаточно свободного места'
else:
    print(f"На накопителе {disk_number + 1} достаточно свободного места.")