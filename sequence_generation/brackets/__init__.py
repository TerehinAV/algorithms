"""
Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n,
упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).

В задаче используются только круглые скобки.

Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных
последовательностей в ответе, и при этом использует объём памяти, пропорциональный n.

Формат ввода
Единственная строка входного файла содержит целое число n, 0 ≤ n ≤ 11

Формат вывода
Выходной файл содержит сгенерированные правильные скобочные последовательности, упорядоченные лексикографически.


Алгоритм:

Для этого будем идти по строке справа налево и поддерживать баланс depth открытых и закрытых скобок
(при встрече открывающей скобки будем уменьшать depth, а при закрывающей — увеличивать).
Если в какой-то момент мы стоим на открывающей скобке, а баланс после обработки этого символа больше нуля,
то мы нашли самую правую позицию, от которой мы можем начать изменять последовательность
(в самом деле, depth > 0 означает, что слева имеется не закрытая ещё скобка).

Поставим в текущую позицию закрывающую скобку, затем максимально возможное количество открывающих скобок,
а затем все оставшиеся закрывающие скобки.
"""

# p = int(input())
p = 5
n = p*2
arr = list("(" * p + ")" * p)

print("".join(arr))
while True:
    # Идем по строке справа налево и поддерживать баланс depth открытых и закрытых скобок
    bracket_index = 0
    depth = 0
    open_count = 0
    close_count = 0
    for i in range(n):
        # при встрече открывающей скобки будем уменьшать depth, а при закрывающей — увеличивать.
        bracket_index = n-1-i
        if arr[bracket_index] == "(":
            open_count += 1
            depth -= 1
        else:
            close_count += 1
            depth += 1
        # Если в какой-то момент мы стоим на открывающей скобке, а баланс после обработки этого символа больше нуля,
        if arr[bracket_index] == "(" and depth > 0:
            # то мы нашли самую правую позицию, от которой мы можем начать изменять последовательность
            # Поставим в текущую позицию закрывающую скобку
            break
    if bracket_index == 0:
        # если не нашли, значит выходим
        break
    arr[bracket_index] = ")"
    # вариант 1
    # затем максимально возможное количество открывающих скобок
    arr[bracket_index+1:bracket_index+1+open_count] = "(" * open_count
    # а затем все оставшиеся закрывающие скобки.
    arr[bracket_index+1+open_count:] = ")" * (close_count - 1)
    print("".join(arr))
    # # вариант 2
    # # затем максимально возможное количество открывающих скобок
    # out = arr[:bracket_index + 1]
    # out += ["("] * (p - out.count("("))
    # # # а затем все оставшиеся закрывающие скобки.
    # out += [")"] * (p - out.count(")"))
    # print("".join(out))
    # arr = out
