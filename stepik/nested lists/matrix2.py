# На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов в матрице.
# Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.
# Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку,
# и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.
# Формат входных данных
# На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут n×m слов, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести считанную матрицу, за ней пустую строку,
# и ту же матрицу, но поменяв местами строки со столбцами. Элементы матрицы разделять одним пробелом.
# # Sample Input:  Sample Output:
# 4               # и швец
# 2               # и жнец
# и               # и на
# швец            # дуде игрец
# и               #
# жнец            # и и и дуде
# и               # швец жнец на игрец
# на
# дуде
# игрец
n, m = int(input()), int(input())
matrix2 = [[0] * n for i in range(m)]
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)
for r in matrix:
    print(*r)
print()
for i in range(m):
    for j in range(n):
        matrix2[i][j] = matrix[j][i]
for c in matrix2:
    print(*c)







