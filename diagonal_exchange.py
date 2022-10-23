# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали,
# при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
# Формат выходных данных
# Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися своими местами.
n = int(input())
matrix = [input().split() for _ in range(n)]
for i in range(n):
    matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]
for c in matrix:
    print(*c)