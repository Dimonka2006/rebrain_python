# Вы получили такую строку логов:
log = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
# Совершите над ней следующие действия:

# 1.1. Выделите и выведите на экран дату и время.
date_time = log[:15]
print("Дата и время:", date_time)

# 1.2. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог.
service_name = log.split()[4]
print("Название сервиса:", service_name)

# 1.3. Замените название ПК (ideapad) на PC-12092, выведите полученную строку на экран.
new_log = log.replace('ideapad', 'PC-12092')
print(new_log)

# 1.4. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.
failed_position = log.find('failed')
if failed_position == -1:
    print("Позиция слова 'failed':", -1)
else:
    print("Позиция слова 'failed':", failed_position)
   
# 1.5. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных).
count_s = sum(1 for char in log if char.lower() == 's')
print("Количество букв 'S':", count_s)
# 1.6. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран.
# это в сумме секунд - в 7.py сложил числа

time_parts = log.split()[2].split(':')
hours = int(time_parts[0])
minutes = int(time_parts[1])
seconds = int(time_parts[2])
total_seconds = hours * 3600 + minutes * 60 + seconds
print(total_seconds)   

# Вы получили такую строку логов:
log2 = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
# Нужно сформировать и вывести сообщение в таком формате:

# The PC "<имя ПК>" receive message from service "<имя сервиса>" what says "<сообщение>" becaus "<причина ошибки>" at <дата, время>

# Разделяем строку на части
parts = log2.split()

# Извлекаем необходимые значения
date_time = f"{parts[0]} {parts[1]} {parts[2]}"

pc_name = parts[3]

service_name = parts[4][:-1]

message = log2.split(':')[3]

error_reason = log2.split(':')[4]

# Формируем итоговое сообщение
output_message = (
    f"The PC \"{pc_name}\" received a message from the service "
    f"\"{service_name}\" which says \"{message}\" because \"{error_reason}\" at {date_time}."
)

print(output_message)