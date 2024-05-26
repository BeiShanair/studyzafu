def f(s):
    result = []
    for i in s:
        if s.count(i) == 1:
            result.append(i)
    return result


a = 'abac'
print(f(a))
