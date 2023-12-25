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
    # print(a)
    n = len(a)
    mxr = 0
    mxg = 0
    mxb = 0
    for i in range(0, n, 2):
        count = int(a[i])
        color = a[i+1]
        # print(count, color, '|')
        if color == 'red':
            mxr = max(mxr, count)
        elif color == 'green':
            mxg = max(mxg, count)
        else:
            mxb = max(mxb, count)
    # print(mxr*mxg*mxb, mxr, mxg, mxb)
    ans += mxr*mxg*mxb
print(ans)
