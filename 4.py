# на вход программе передается 3х значное число
# вывести результат произведения всех разрядов числа

# вывод: 123
# вывод: 6

# вывод: 424
# вывод: 32

n = int(input())
ones = n % 10
tens = n // 10 % 10
hunds = n // 100
print(ones * tens * hunds) 

# var2
n = input()
print(int(n[0]) * int(n[1]) * int(n[2]))