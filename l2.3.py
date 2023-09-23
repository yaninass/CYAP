def poisk(matrix):
    zero_row_index = None
    for i, row in enumerate(matrix):#проходим по строке матрицы и каждому элементу строки
        if all(elem == 0 for elem in row):
            zero_row_index = i
            break
    if zero_row_index is not None:
        for row in matrix:
            row[zero_row_index] /= 2

    return matrix


def input_matrix():
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))

    matrix = []

    for i in range(n):
        row = list(map(int, input(f"Введите {m} чисел строки {i + 1}, разделенные пробелами: ").split()))
        matrix.append(row)
    return matrix


matrix = input_matrix()
print("Ваша матрица")
for row in matrix:
    print(row)
new_matrix = poisk(matrix)
print("Ваша матрица")
for row in new_matrix:
    print(row)
