import random
a = []
for i in range(20):
    a.append(random.randint(1000, 5000))

print(a)
su_shu = (2, 3, 5, 7)
for i in su_shu:
    for j in a:
        if j % i != 0:
            print(j, end=" ")
            break
