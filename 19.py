# Вам дан тот самый, уже полюбившийся вам список логов из 3, 5 или 6 блока:
log_lines = [
    'May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
    'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
    'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
    'May 20 11:01:12 PC-00102 PackageKit: daemon start',
    'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
    'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
    'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
    'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
    'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
    'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
    'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.'
]
# Напишите функцию, которая:
# 2.1. Получает в качестве первого аргумента список для вывода данных, а в качестве последующих - сколько угодно строк логов по типу тех, что есть в скопированном вами списке.

# 2.2. Превращает вводимые вами строки логов в словари по тому же принципу, что и в пункте 2 задания для 3го блока. Напоминаю:

# 'time': <дата/время>
# 'pc_name': <имя компьютера>
# 'service_name': <имя сервиса>
# 'message': <сообщение лога>
# 2.3. Модифицирует входной список (переданный в качестве первого аргумента), добавляя в него все созданные словари. Возвращать функция, соответственно, должна None

# 2.4. Создайте пустой список и добавьте в него 1ю, 2ю и 4ю запись из списка логов с помощью одного вызова вашей функции. Выведите полученный список на экран

# Скопируйте к себе этот модифицированный список из 4го блока, отображающий количество общей и занятой памяти на накопителях:
list_info = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]
# Напишите функцию, которая:
# 4.1. Получает этот список

# 4.2. Анализирует состояние памяти каждого накопителя по алгоритму из задания для 4го блока. Напоминаю:

# Если свободной памяти осталось меньше 10Гб или меньше 5%, то на накопителе критически мало свободного места;
# Если свободной памяти больше, чем в предыдущем пункте, но меньше 30Гб или меньше 10%, то на накопителе мало свободного места;
# Иначе на накопителе достаточно свободного места
# 4.3. Формирует словарь, ключами которого являются: 'memory_ok', 'memory_not_enough' и 'memory_critical', а значениями - списки id накопителей, состояние которых относится к соответствующему ключу (достаточно свободного места, мало свободного места и критически мало свободного места соответственно).

# 4.4. Возвращает сформированный словарь.

# Примените эту функцию к вашему списку и выведите словарь, полученный в результате ее работы, на экран.


# 2.1
output_list = []
def process_log_lines(output_list, *log_lines):
    for log_line in log_lines:

        line = log_line.split(maxsplit=3)
        
        if len(line) == 4:
            time, pc_name, service_name, message = line
        else:
            print(f'Ошибка при разборе строки: {log_line}')
            continue
#2.2            
def get_line_dict(line: str) -> dict:
    time_field = line[:15]
    fields = line[16:]
    div = fields.find(":")
    message = fields[div+1:]
    pc_name, service = fields[:div].split()

    return {
            "time": time_field.strip(),
            "pc_name": pc_name.strip(),
            "service_name": service.strip(),
            "message": message.strip()
            }

log_dict = [get_line_dict(line) for line in log_lines]
#2.3        
        output_list.append(log_dict)

    return None
#2.4
new_log_list = []

process_log_lines(new_log_list, log_lines[0], log_lines[1], log_lines[3])

print(new_log_list)



