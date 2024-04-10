def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


a = int(input("请输入一个整数："))
if a % 2 != 0 or a < 3:
    print("Data Error!")
else:
    for i in range(4, a + 1, 2):
        for j in range(2, i):
            if prime(j) and prime(i - j):
                print("{:^4} = {:^4} + {:^4}".format(i, j, i - j))
                break
