# Следом квадратной матрицы называется сумма элементов главной диагонали.
# Напишите программу, которая выводит след заданной квадратной матрицы.
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
# Формат выходных данных
# Программа должна вывести одно число — след заданной матрицы.
# Sample Input:    Sample Output:
# 3                    15
# 1 2 3
# 4 5 6
# 7 8 9
x = int(input())
sum1 = 0
matrix = []
for i in range(x):
    matrix.append(input().split())
for i in range(len(matrix)):
    sum1 += int(matrix[i][i])
print(sum1)
