lines = list(open('11.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

a = []
for line in lines:
    a.append(line)

n = len(a)
m = len(a[0])
r = []
c = []
for i in range(n):
    r.append(True)
for i in range(m):
    c.append(True)
g = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '#':
            g.append((i, j))
            r[i] = False
            c[j] = False
r1 = [0]
cur = 0
for i in range(n):
    cur += 1
    if r[i]:
        cur += 999999
    r1.append(cur)
c1 = [0]
cur = 0
for i in range(m):
    cur += 1
    if c[i]:
        cur += 999999
    c1.append(cur)
gn = len(g)
ans = 0
print(g)
for i in range(gn):
    for j in range(i + 1, gn):
        i1 = g[i][0] + 1
        j1 = g[i][1] + 1
        i2 = g[j][0] + 1
        j2 = g[j][1] + 1
        print(i1, j1, i2, j2)
        print(r1[i1], c1[j1], r1[i2], c1[j2])
        if i2 > i1:
            print('i:', r1[i2] - r1[i1 - 1])
            ans += r1[i2] - r1[i1 - 1]
        elif i2 < i1:
            print('i:', r1[i1] - r1[i2 - 1])
            ans += r1[i1] - r1[i2 - 1]
        if j2 > j1:
            print('j:', c1[j2] - c1[j1 - 1])
            ans += c1[j2] - c1[j1 - 1]
        elif j2 < j1:
            print('j:', c1[j1] - c1[j2 - 1])
            ans += c1[j1] - c1[j2 - 1]
        if i1 != i2:
            ans -= 1
        if j1 != j2:
            ans -= 1
print(ans)
