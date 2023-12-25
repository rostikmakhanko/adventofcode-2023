def is_digit(c):
    return c >= '0' and c <= '9'

lines = list(open('3.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
n = len(lines)
m = len(lines[0])
se = '.' * m
lines.insert(0, se)
lines.append(se)
for i in range(n+2):
    lines[i] = '.' + lines[i] + '.'
n += 2
m += 2
a = []
for i in range(n):
    a1 = []
    for j in range(m):
        a1.append([])
    a.append(a1)
a[0][0].append(123)

def check(row, start, end, value):
    for i in range(row - 1, row + 2):
        for j in range(start - 1, end + 2):
            if lines[i][j] == '*':
                a[i][j].append(value)

for i in range(n):
    s = lines[i]
    cur = ''
    start = 0
    # print(i, m, s, len(s))
    for j in range(m):
        if is_digit(s[j]):
            cur += s[j]
        else:
            end = j - 1
            if cur != '':
                value = int(cur)
                check(i, start, end, value)
            cur = ''
            start = j + 1
ans = 0
for i in range(n):
    s = lines[i]
    for j in range(m):
        if s[j] == '*':
            if len(a[i][j]) == 2:
                ans += a[i][j][0] * a[i][j][1]
print(ans)
    