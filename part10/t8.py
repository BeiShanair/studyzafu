
x = [range(3*i, 3*i+5) for i in range(2)]

print(x)

x = list(map(list, x))


print(x)
x = list(map(list, zip(*x)))

print(x)