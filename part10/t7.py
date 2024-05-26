from random import randint

result = set()
while True:
    result.add(randint(1, 10))
    if len(result) == 20:
        break
print(result)
