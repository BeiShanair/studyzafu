def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


count = 0
for i in range(3, 101):
    if prime(i):
        print("{:<4}".format(i), end="")
        count += 1
        if count % 5 == 0:
            print()
