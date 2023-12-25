lines = list(open('9.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

ans = 0
for line in lines:
    a = line.split()
    a = list(map(lambda x: int(x), a))
    firsts = []
    while len(a) > 0 and a.count(0) < len(a):
        n = len(a)
        firsts.append(a[0])
        b = []
        for i in range(1, n):
            b.append(a[i] - a[i-1])
        a = b.copy()
    firsts.append(0)
    cur = 0
    for i in range(len(firsts)-2, -1, -1):
        cur = firsts[i] - cur
    ans += cur
print(ans)