"""
Реализация генератора правильных скобочных последовательностей упорядоченных в обратном лексеграфическом порядке

Генерацию очередной скобочной последовательности будем делать следующим образом:
- просматриваем последовательность справа налево до первой комбинации скобок )(. Такая
комбинация будет в любой последовательности, кроме последней;
- найденную комбинацию надо заменить на ();
- подсчитываем с начала строки, на сколько число открывающихся скобок больше числа
закрывающихся и дописываем это количество закрывающихся скобок начиная от индекса найденной "(" из пары предыдущего
пункта;
- если длина строки еще не стала равна 2*n, то ее необходимо дополнить нужным количеством пар скобок ().
"""

p = input()
n = p * 2

arr = ["(", ")"] * p
# print("".join(arr))
reversed_sorted_brackets_list = list()
reversed_sorted_brackets_list.append("".join(arr))
while True:
    bracket_index = 0
    for i in range(n):
        # - просматриваем последовательность справа налево до первой комбинации скобок )(. Такая
        # комбинация будет в любой последовательности, кроме последней;
        bracket_index = n - 1 - i
        if arr[bracket_index] == "(" and arr[bracket_index-1] == ")":
            # - найденную комбинацию надо заменить на ();
            arr[bracket_index] = ")"
            arr[bracket_index-1] = "("
            break
    if bracket_index == 0:
        break
    # - подсчитываем с начала строки, на сколько число открывающихся скобок больше числа
    # закрывающихся и дописываем это количество закрывающихся скобок начиная от индекса найденной "("
    # из пары предыдущего пункта;
    open_count = arr[:bracket_index+1].count("(")
    close_count = arr[:bracket_index+1].count(")")
    depth = open_count - close_count
    out = arr[:bracket_index+1]
    out += [")"] * depth
    delta = len(arr) - len(out)
    if delta == 0:
        reversed_sorted_brackets_list.append("".join(out))
        arr = out
        continue
    # - если длина строки еще не стала равна 2*n, то ее необходимо дополнить нужным количеством пар скобок ().
    out += ["(", ")"] * (delta // 2)
    reversed_sorted_brackets_list.append("".join(out))
    arr = out

# обратная последовательность
# list(map(print, reversed_sorted_brackets_list))
# прямая
list(map(print, reversed_sorted_brackets_list[::-1]))