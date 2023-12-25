lines = list(open('4.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
n = len(lines)
a = []
b = []
for line in lines:
    start = line.find(':') + 2
    s = line[start:]
    p = s.find('|')
    a1 = s[:p - 1]
    b1 = s[p + 2:]
    a.append(a1.split())
    b.append(b1.split())
    # print(a1.split(), b1.split())
ans = []
for i in range(n):
    ans.append(1)
for i in range(n):
    k = 0
    for bx in b[i]:
        if bx in a[i]:
            k += 1
    if k > 0:
        f = i + 1
        t = i + k
        for j in range(f, min(t + 1, n)):
            ans[j] += ans[i]
ans1 = 0
for x in ans:
    ans1 += x
print(ans1)
