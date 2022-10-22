# На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
# Программа должна вывести указанный вложенный список.
# Sample Input: w w w o r l d g g g g r e a t t e c c h e m g g p w w Sample Output: [['w', 'w', 'w'], ['o'], ['r'], ['l'],
# ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'],
# ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]
n = input().split()
x = [[n[0]]]
for i in range(1, len(n)):
    if n[i] != n[i - 1]:
        x.append([n[i]])
    elif n[i] == n[i - 1]:
        x[-1].append(n[i])
print(x)