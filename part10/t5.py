def s(num):
    if num < 0:
        return 0
    elif num < 5:
        return num
    elif num < 10:
        return num * 3 - 5
    elif num < 20:
        return num * 0.5 - 2
    else:
        return 0


a = int(input())
print(s(a))
