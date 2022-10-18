n = input().split()
x = [[n[0]]]
for i in range(1, len(n)):
    if n[i] != n[i - 1]:
        x.append([n[i]])
    elif n[i] == n[i - 1]:
        x[-1].append(n[i])
print(x)