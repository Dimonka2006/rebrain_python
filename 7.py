log = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'

# Разбиваем строку на список элементов
parts = log.split()

# Извлекаем часы, минуты и секунды
hours = int(parts[2].split(':')[0])


minutes = int(parts[2].split(':')[1])


seconds = int(parts[2].split(':')[2])

# Суммируем часы, минуты и секунды
total = hours + minutes + seconds


print(total)
