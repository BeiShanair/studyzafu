def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


num = int(input("请输入一个大于2的偶数："))
if num % 2 != 0 and num < 4:
    print("Data error!")
else:
    for j in range(2, num):
        if prime(j) and prime(num - j) and j < num - j:
            print("{:^4} = {:^4} + {:^4}".format(num, j, num - j))
