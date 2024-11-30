# Дан файл 17.txt с текстом - словами,
# Разделенными пробелами  переносами строк
# Провести частотный анализ файла.
with open('17.txt') as f:
    words = f.read().split()
    #words = words.split()
print(words)
frequency = {}
for w in words:
    for ch in w:
        # if ch in frequency:
        #     frequency[ch] += 1
        # else:
        #     frequency[ch] = 0     
        frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)
print(*sorted([(i[1], i[0]) for i in frequency.items()]))
print(*sorted([(i[1], i[0]) for i in frequency.items()], reverse=True))
print(*sorted([(i[1], i[0]) for i in frequency.items()], reverse=True), sep='\n')