# В программе определен список чисел 
# ежечастные показания температуры умного градусника
# Пользователь вводит 2 положительных числа - начальный и конечные часы
# если средняя температура меду этими часми 
# выше 15 градусов, вывести "Warm"
# если от 5 до 15, вывести "Narmal"
# если ниже 5, вывести "Cold"
# если список пуст, вывести "No info"  

temperatures = [3, 3, 2, 1, 0, -2, -5, 0]
start_h = int(input())
end_h = int(input())
if len(temperatures):
    measure_hs = temperatures[start_h:end_h + (1 if end_h != len(temperatures) - 1 else 0)]
    avg_t = sum(measure_hs) / len(measure_hs)
    if avg_t > 15:
        print('Warm')
    elif 5 <= avg_t <= 15:
        print('Normal')
    else:
        print('Cold')
else:
     print('No info')