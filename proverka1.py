logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
data_time = logs.split()
data_time_pr = ' '.join(data_time[0:3])
print('Дата и время:', data_time_pr)

logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
service = logs.split()
service_systemd = service[4].split(':')[0]
print('Название сервиса:', service_systemd )


logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
logs_new = logs.replace('ideapad', 'PC-12092')
print(logs_new)


logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
if 'failed' in logs:
    print(logs.find('failed'))
else:
    print('-1')
