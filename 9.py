lines = list(open('9.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

ans = 0
for line in lines:
    a = line.split()
    a = list(map(lambda x: int(x), a))
    lasts = []
    while len(a) > 0 and a.count(0) < len(a):
        n = len(a)
        lasts.append(a[n-1])
        b = []
        for i in range(1, n):
            b.append(a[i] - a[i-1])
        a = b.copy()
    ans += sum(lasts)
print(ans)
        