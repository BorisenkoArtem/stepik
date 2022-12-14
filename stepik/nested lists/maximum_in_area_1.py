# Напишите программу, которая выводит максимальный элемент в нижней части ,разделенного диаганалью, квадрата.
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
# Примечание. Элементы главной диагонали также учитываются.
# Sample Input:   Sample Output:
# 3               # 7
# 1 4 5
# 6 7 8
# 1 1 6
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

largest = matrix[0][0]

for i in range(n):
    for j in range(i + 1):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
print(largest)