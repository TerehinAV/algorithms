"""
Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.

Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный объем
памяти в процессе работы.
"""

out = ''
with open('input.txt', 'r') as f:
    vec_size = int(f.readline())
    i = 1
    num = int(f.readline())
    print(num)
    while i <= vec_size:
        line = f.readline()
        if not line:
            break
        next_num = int(line)
        if next_num != num:
            print(next_num)
            num = next_num
        i += 1
