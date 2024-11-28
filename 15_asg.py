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


log_dictionaries = [get_line_dict(line) for line in log_lines]
times = [dictionary["time"] for dictionary in log_dictionaries]
print(times)

from copy import deepcopy

log_dict1 = deepcopy(log_dictionaries)

for dictionary in log_dict1:
    date_and_time = dictionary["time"].split()
    dictionary["date"] = date_and_time[0:2]
    dictionary["time"] = date_and_time[2:]

# а здесь можно было и по-другому сделать
def datetime_to_date_time(data: dict) -> dict:
    _datetime = data["time"].split()
    data["date"] = _datetime[0:2]
    data["time"] = _datetime[2:]
    return data
log_dict2 = deepcopy(log_dictionaries)
# если использовать списковое включение и функцию
changed_date_time = [ datetime_to_date_time(d) for d in log_dict2 ]
print(f"=============> changed_date_time = {changed_date_time}")
# можно использовать map  например
log_dict3 = deepcopy(log_dictionaries)
# map применяет функцию ко всем элементам
changed_date_time2 = list(map(datetime_to_date_time, log_dict3))
print(f"=============> changed_date_time2 = {changed_date_time2}")

new_times = [dictionary["time"] for dictionary in log_dictionaries]
print(new_times)

messages_from_pc_0078 = [dictionary["message"] for dictionary in log_dictionaries if dictionary["pc_name"] == "PC0078"]
print(messages_from_pc_0078)
# а здесь можно было использовать функцию filter и анонимную функцию
_filtered_messages = list(filter(lambda x: x["pc_name"] == "PC0078", log_dictionaries))
print(f"=============> _filtered_messages =  {_filtered_messages}")

log_dictionary_map = {i + 100: dictionary for i, dictionary in enumerate(log_dictionaries)}
print(log_dictionary_map[104])
