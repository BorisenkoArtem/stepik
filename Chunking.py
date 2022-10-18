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