def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


count = 0
for num in range(3, 100):
    if prime(num):
        print(num, end=" ")
        count += 1
        if count % 5 == 0 and count != 0:
            print()
