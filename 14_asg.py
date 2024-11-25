resource = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]
# Запрашивает у пользователя номер накопителя, который нужно проверить.
n = len(resource)
while True:
    user_input = input(f"Введите номер накопителя, который нужно проверить от 1 до {n}: ")
    if not user_input.isnumeric():
        print("Необходимо ввести номер накопителя")
        continue
    disk_number = int(user_input) - 1 # счет начинается с 0
    if disk_number >= len(resource) or disk_number < 0:
        print(f"Необходимо ввести число от 1 до {n}")
        continue
    break
