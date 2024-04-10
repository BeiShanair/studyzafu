count = 0
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        if count % 5 == 0:
            print()
        print("{:<5}".format(num), end="")
        count += 1
print("\n共有", count, "个素数")
