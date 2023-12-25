def get_ans(a):
    n = len(a)
    m = len(a[0])
    ans = 0
    for i in range(n-1):
        i1 = i
        i2 = i + 1
        while i1 >= 0 and i2 < n:
            # print(i1, i2)
            if a[i1] != a[i2]:
                break
            else:
                i1 -= 1
                i2 += 1
        if i1 == -1 or i2 == n:
            ans = max(ans, i+1)
    return ans

def get_a_traversed(a):
    n = len(a)
    m = len(a[0])
    b = []
    for j in range(m):
        s = ""
        for i in range(n):
            s += a[i][j]
        b.append(s)
    return b

lines = list(open('13.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

a = []
ans = 0
for line in lines:
    if line == "":
        ans += max(get_ans(get_a_traversed(a)), get_ans(a) * 100)
        a = []
        # print(ans)
    else:
        a.append(line)
ans += max(get_ans(get_a_traversed(a)), get_ans(a) * 100)
print(ans)