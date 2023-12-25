def  get_calibrattion_number(s):
    first = '-'
    last = '-'
    n = len(s)
    for i in range(n):
        if s[i] >= '0' and s[i] <= '9':
            first = s[i]
            break
    for i in range(n - 1, -1, -1):
        if s[i] >= '0' and s[i] <= '9':
            last = s[i]
            break
    return int(first+last)

lines = tuple(open('1.txt', 'r'))
ans = 0
for line in lines:
    # print(get_calibrattion_number(line))
    ans += get_calibrattion_number(line)
print(ans)