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
