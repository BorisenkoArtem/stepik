# объявление функции
def is_valid_password(password):
    total = 0
    f1, f2, f3 = False, False, False
    x = [c for c in password.split(":")]
    if len(x) == 3:
        if x[0] == x[0][::-1]:
            f1 = True
        for i in range(int(x[1])):
            if int(x[1]) % (i + 1) == 0:
                total += 1
        if total == 2:
            f2 = True
        if int(x[2]) % 2 == 0:
            f3 = True
    if f1 == True and f2 == True and f3 == True:
        return True
    else:
        return False
# считываем данные
psw = input()
# вызываем функцию
print(is_valid_password(psw))

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))