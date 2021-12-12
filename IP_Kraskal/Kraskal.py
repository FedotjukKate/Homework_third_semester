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


matrix = [[0, 4, 0, 0, 0, 0, 0, 0, 8], [4, 0, 8, 0, 0, 0, 0, 0, 11], [0, 8, 0, 7, 0, 4, 0, 2, 0],
          [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 6, 1], [0, 0, 2, 0, 0, 0, 6, 0, 7], [8, 11, 0, 0, 0, 0, 1, 7, 0]]
lst = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] != 0 and j > i:
            lst.append((i + 1, j + 1, matrix[i][j]))
lst = sorted(lst, key=lambda x: x[2])
lst_1 = []
ls = []
P = True
for i in range(len(lst)):
    if i == 0:
        lst_1.append(lst[i])
        ls.append(lst[i][0])
        ls.append(lst[i][1])
    elif lst[i][0] not in ls and lst[i][1] in ls:
        elem = lst[i][2]
        p = lst[i]
        for line in lst:
            if line[0] == lst[i][0] and line != lst[i] and line[1] in ls:
                if line[2] < elem:
                    elem = line[2]
                    p = line
            elif line[1] == lst[i][0] and line != lst[i] and line[0] in ls:
                if line[2] < elem:
                    elem = line[2]
                    p = line
        lst_1.append(p)
        ls.append(p[0])
    elif lst[i][1] not in ls and lst[i][0] in ls:
        elem = lst[i][2]
        p = lst[i]
        for line in lst:
            if line[1] == lst[i][1] and line != lst[i] and line[0] in ls:
                if line[2] < elem:
                    elem = line[2]
                    p = line
            elif line[0] == lst[i][1] and line != lst[i] and line[1] in ls:
                if line[2] < elem:
                    elem = line[2]
                    p = line
        lst_1.append(p)
        ls.append(p[1])
matrix_2 = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        for line in lst_1:
            if i + 1 == line[0] and j + 1 == line[1]:
                matrix_2[i][j] = line[2]
            elif j + 1 == line[0] and i + 1 == line[1]:
                matrix_2[i][j] = line[2]
for _ in range(len(matrix)):
    print(matrix_2[_])
