def get_indices(lst, elem):
    return [i for i in range(len(lst)) if lst[i] == elem]


# для того чтобы пользователь вводил матрицу можно взять код с Deikstra.py
matrix = [[0, 12, 10, 0, 0, 0, 0, 0, 0], [0, 0, 9, 0, 3, 1, 0, 0, 0], [0, 0, 0, 8, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 5, 8, 0], [0, 0, 0, 7, 0, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0, 6, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 9, 11], [0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
a = int(input("От какой вершины:"))
b = int(input("До какой вершины:"))
lst = []
lst_chek = []
lst_doroga = []
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
    count = 0
    for k in range(len(lst)):
        lst_1 = matrix[c]
        if k != c:
            if lst_1[k] + lst[c] < lst[k] and lst_1[k] != 0:
                lst[k] = lst_1[k] + lst[c]
                if i == 0:
                    lst_doroga.append([(a, 0), (k + 1, lst[k])])
                elif count == 0:
                    for t, ind in enumerate(lst_doroga):
                        if (c + 1, lst[c]) == lst_doroga[t][-1]:
                            lst_doroga.append(lst_doroga[t][:])
                            lst_doroga[-1].append((k + 1, lst_1[k] + lst[c]))
                            count += 1
                else:
                    for t, ind in enumerate(lst_doroga):
                        if (c + 1, lst[c]) == lst_doroga[t][-2]:
                            lst_doroga.append(lst_doroga[t][:-1])
                    lst_doroga[-1].append((k + 1, lst_1[k] + lst[c]))
        lst_chek[c] = 1


if lst[b - 1] != 10 ** 10:
    print(f"кратчайший путь = {lst[b - 1]}")
else:
    print("Нет такого пути")
lst_ver = []
for i in range(len(lst_doroga)):
    for j in range(len(lst_doroga[i])):
        if lst_doroga[i][-1][0] == b and lst_doroga[i][j][1] == lst[b - 1]:
            for t in range(len(lst_doroga[i])):
                lst_ver.append(str(lst_doroga[i][t][0]))
print("-".join(lst_ver))