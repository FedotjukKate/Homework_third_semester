def get_indices(lst, elem):
    return [i for i in range(len(lst)) if lst[i] == elem]


def matrix_in():
    ctr = int(input("Введите колличество вершин:"))
    matrix = []
    for i in range(ctr):
        print(
            f"Введите ЧЕРЕЗ ПРОБЕЛ расстояния дорог ВЫХОДЯЩИХ из вершины "
            f"{i + 1} до других вершин, если дороги нет введите 0")
        l = input().split(" ")
        matrix.append([int(num) for num in l])
    return matrix


# пользователь сам вводит матрицу
# matrix = matrix_in()

matrix = [[0, 7, 9, 0, 0, 14], [0, 0, 10, 15, 0, 0], [0, 0, 0, 11, 0, 2],
          [0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 9, 0]]
a = int(input("От какой вершины:"))
lst = []
lst_chek = []
for i in range(len(matrix)):
    if i == (a - 1):
        lst.append(0)
    else:
        lst.append(10 ** 10)
    lst_chek.append(0)
c = lst.index(min(lst))
for i in range(len(matrix)):
    p = []
    for j in range(len(lst_chek)):
        if j in get_indices(lst_chek, 0):
            p.append(lst[j])
        else:
            p.append(10 ** 10)
    c = p.index(min(p))
    p = []
    for k in range(len(lst)):
        lst_1 = matrix[c]
        if k != c:
            if lst_1[k] + lst[c] < lst[k] and lst_1[k] != 0:
                lst[k] = lst_1[k] + lst[c]
        lst_chek[c] = 1
for i in range(len(lst)):
    if lst[i] != 10 ** 10 and lst[i] != 0:
        print(f"Расстояние от {a} до {i + 1} равно {lst[i]}")
    elif lst[i] != 0:
        print(f"От {a} до {i + 1} дороги нет")
