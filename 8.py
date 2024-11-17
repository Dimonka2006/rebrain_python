log2 = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'

# Разделяем строку на части
parts = log2.split()

# Извлекаем необходимые значения
date_time = f"{parts[0]} {parts[1]} {parts[2]}"
pc_name = parts[3]
service_name = parts[4][:-1]  # Убираем закрывающуюся скобку
message = ' '.join(parts[7:])
error_reason = 'Нет доступных данных'  # Так как причина всегда одна и та же

# Формируем итоговое сообщение
output_message = (
    f"The PC \"{pc_name}\" received a message from the service "
    f"\"{service_name}\" which says \"{message}\" because \"{error_reason}\" at {date_time}."
)

print(output_message)
