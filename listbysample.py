n = int(input())
my_list = []
for i in range(n):
    my_list.append(list(range(1, i + 2)))
print(*my_list, sep="\n")
