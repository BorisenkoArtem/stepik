# На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.
# Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.
# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число n на отдельной строке.
# Формат выходных данных
# Программа должна вывести указанный вложенный список.
# Sample Input 1: a b c d e f # 2  Sample Output 1:  [['a', 'b'], ['c', 'd'], ['e', 'f']]
def chunked(word, num):
    p = []
    l = []
    if len(word) <= num:
        return [word]
    else:
        for i in range(len(word)):
            p.append(word[i])
            if len(p) == num:
                l.append(p)
                p = []
        if len(word) % num > 0:
            z = len(word) % num
            l.append(word[-z:])
        return l
word = input().split()
num = int(input())
print(chunked(word, num))