r_max = 12
g_max = 13
b_max = 14

def can(count, color):
    if color == 'red':
        if count > r_max:
            return False
    elif color == 'green':
        if count > g_max:
            return False
    else:
        if count > b_max:
            return False
    return True

lines = tuple(open('2.txt', 'r'))
i1 = 0
ans = 0
for line in lines:
    i1 += 1
    p_start = line.find(':') + 2
    s = line[p_start:]
    s = s.replace('\n', '')
    s = s.replace(';', '')
    s = s.replace(',', '')
    a = s.split(' ')
    n = len(a)
    possible = True
    for i in range(0, n, 2):
        count = int(a[i])
        color = a[i+1]
        # print(count, color)
        if not can(count, color):
            possible = False
            break
    if possible:
        # print(i1)
        ans += i1
print(ans)
