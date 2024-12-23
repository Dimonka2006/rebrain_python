
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
# 2.1. Создайте алгоритм заполнения словаря, подходящий для любой строчки лога. Словарь должен содержать в себе такую информацию:

# 'time': <дата/время>
# 'pc_name': <имя компьютера>
# 'service_name': <имя сервиса>
# 'message': <сообщение лога>

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

for line in log_lines:
    line_dict = get_line_dict(line)
    print(line_dict)

# 2.2. Заполните словарь для одной из строк лога с помощью данного алгоритма, запросив у пользователя номер строки с помощью input().

for line in log_lines:
    index = int(input("Введите номер строки: "))
    line = log_lines[index]
    line_dict = get_line_dict(line)
    print(line_dict)

# Выведите на экран информацию из текущего словаря в таком виде:
# <имя компьютера>: <сообщение>

    output_format = "{}: {}"
    print(output_format.format(line_dict["pc_name"], line_dict["message"]))
    break

# 3.1. Список
literal_list = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']

# 3.2. Создайте список ключей из 2.1.
keys = ['time', 'pc_name', 'service_name', 'message']

# 3.3. Используя функцию zip(), создайте словарь из этих двух списков
result_dict = dict(zip(keys, literal_list))
print(result_dict)

# 4. Создайте список словарей: из словаря, который вы получили в пункте 2 и словаря из пункта 3 (в итоге у вас должен получиться список, состоящий из двух словарей). 
# Выведите полученный список на экран

list_of_dict = [line_dict, result_dict]
print(list_of_dict)

# 5. Используя преобразование во множество, выведите список совпадающих значений полученных словарей.

set_values_1 = set(line_dict.values())
set_values_2 = set(result_dict.values())

common_values = set_values_1.intersection(set_values_2)
common_values_list = list(common_values)

print(common_values_list)
