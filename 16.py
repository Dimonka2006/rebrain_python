# Даны два файла, 16_1.txt и 16_2.txt
# Обьеденить их содержимое в in1.txt
with open('16_1.txt', 'a', encoding='utf-8') as f16_1, open('16_2.txt', 'a', encoding='utf-8') as f16_2:
    f16_1.write('\n')
    for line in f16_2:
        f16_1.write(line)    