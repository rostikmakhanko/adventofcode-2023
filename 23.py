import sys
sys.setrecursionlimit(100000)

lines = list(open('23.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

a = []
visited = []
for line in lines:
    x = []
    for c in line:
        x.append(False)
    visited.append(x)
    a.append(list(line))

n = len(a)
m = len(a[0])

def go(i0, j0, i1, j1, k):
    if i1 < 0 or j1 < 0 or i1 >= n or j1 >= m:
        return 0
    if a[i1][j1] == '#':
        return 0
    if i1 == n-1 and j1 == m-2:
        return k
    if a[i1][j1] == '>':
        return go(i1, j1, i1, j1+1, k+1)
    elif a[i1][j1] == 'v':
        return go(i1, j1, i1+1, j1, k+1)
    ans = k+1
    if i1-1 != i0 and i1 > 0:
        if a[i1-1][j1] != 'v':
            ans = max(ans, go(i1, j1, i1-1, j1, k+1))
    if j1-1 != j0 and j1 > 0:
        if a[i1][j1-1] != '>':
            ans = max(ans, go(i1, j1, i1, j1-1, k+1))
    if i1+1 != i0:
        ans = max(ans, go(i1, j1, i1+1, j1, k+1))
    if j1+1 != j0:
        ans = max(ans, go(i1, j1, i1, j1+1, k+1))
    return ans

print(go(-1, 1, 0, 1, 0))
    