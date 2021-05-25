# Эта функция возвращает элемент, дубликат которого имеет следующий порядковый номер(как в примере)
def next_elem_repeat(a):
    try:
        tmp = 0
        for j in a:
            if j == a[tmp + 1]:
                return j
            else:
                tmp += 1
    except Exception("There are no expected duplicates"):
        return Exception


print(next_elem_repeat(["a", "b", "c", "b", "a", "d", "d"]))


# Эта функция возвращает элемент с наименьшим порядковым номером имеющий дубликат в списке
def return_first_repeat(a):
    try:
        tmp = 0
        for i in range(len(a) - 1):
            for j in a[tmp + 1:]:
                if a[tmp] == j:
                    return j
            tmp += 1
    except Exception("There is no duplicates"):
        return Exception


print(return_first_repeat(["A", "B", "B" "c", "A"]))
