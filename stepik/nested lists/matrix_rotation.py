# Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘по часовой стрелке.
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
# Формат выходных данных
# Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.
n = int(input())
matrix = [input().split() for _ in range(n)]
matrix1 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix1[i][j] = matrix[n - 1 - j][i]
for c in matrix1:
    print(*c)
