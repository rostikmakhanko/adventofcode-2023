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

def check(row, start, end):
    for i in range(row - 1, row + 2):
        for j in range(start - 1, end + 2):
            if not is_digit(lines[i][j]) and lines[i][j] != '.':
                return True

ans = 0
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
                add = int(cur) if check(i, start, end) else 0
                ans += add
            cur = ''
            start = j + 1
print(ans)
    