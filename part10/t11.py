def f(s):
    if not s.isdigit():
        return '不是数字字符串'
    s = s[::-1]
    result = ''
    for i in range(0, len(s), 3):
        result += s[i:i + 3] + ','
    return result[::-1].strip(',')


a = input()
print(f(a))
