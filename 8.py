lines = list(open('8.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

n = len(lines)
s = lines[0]
g = {}
for i in range(2, n):
    s1 = lines[i]
    cur = s1[:3]
    left = s1[7:10]
    right = s1[12:15]
    # print(cur, left, right)
    g[cur] = (left, right)
ans = 0
cur = "AAA"
s = s * 1000
for c in s:
    ans += 1
    if c == 'L':
        cur = g[cur][0]
    else:
        cur = g[cur][1]
    if cur == "ZZZ":
        # print(ans)
        break
print(ans)