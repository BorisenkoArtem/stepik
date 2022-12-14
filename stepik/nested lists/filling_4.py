# # На вход программе подается натуральное число n.
# # Напишите программу, которая создает матрицу размером n×n заполнив её в соответствии с образцом.
# # Формат входных данных
# # На вход программе подается натуральное число n — количество строк и столбцов в матрице.
# # Формат выходных данных
# # Программа должна вывести указанную матрицу в соответствии с образцом:
# # разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.
# # Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
# # Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
# Sample Input:     Sample Output:
# 5                 1  1  1  1  1
#                   0  1  1  1  0
#                   0  0  1  0  0
#                   0  1  1  1  0
#                   1  1  1  1  1

n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j >= i <= n - 1 - j  or j <= i >= n - 1 - j:
            matrix[i][j] = 1
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()