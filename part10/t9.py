def s(num):
    if num == 0:
        return 1
    else:
        return len(bin(num)) - len(bin(num).rstrip('0'))


a = int(input())
print(s(a))
