import sys
sys.setrecursionlimit(1000000)

lines = list(open('10.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
n = len(lines)
m = len(lines[i])
all = n*m
a = []
b = []
s_dots = '.'.join('.' * (m+2))
a.append('.' * (m+2))
b.append(s_dots)
b.append(s_dots)
for line in lines:
    a.append('.' + line + '.')
    b.append(s_dots)
    b.append(s_dots)
a.append('.' * (m+2))
b.append(s_dots)
b.append(s_dots)
b_ans = b.copy()
n += 2
m += 2
visited = []
for i in range(n):
    arr = []
    for j in range(m):
        arr.append(False)
    visited.append(arr)

def dfs_prep(i, j, d, i0, j0):
    bi = list(b[i0*2])
    bi[j0*2] = '*'
    b[i0*2] = ''.join(bi)
    bi = list(b[i*2])
    bi[j*2] = '*'
    b[i*2] = ''.join(bi)
    mid_i = (i*2+i0*2)//2
    mid_j = (j*2+j0*2)//2
    print(i, j, i0, j0, mid_i, mid_j, b[mid_i][mid_j])
    bi = list(b[mid_i])
    bi[mid_j] = '*'
    b[mid_i] = ''.join(bi)
    if visited[i][j]:
        if a[i][j] == 'S':
            print(d)
            global b_ans
            b_ans = b.copy()
            pass
        return
    visited[i][j] = True
    dfs(i, j, d)
    print("THATS IT")
    # bi = list(b[i*2])
    # bi[j*2] = '.'
    # b[i*2] = ''.join(bi)
    # bi = list(b[mid_i])
    # bi[mid_j] = '.'
    # b[mid_i] = ''.join(bi)

def dfs(i, j, d):
    # print(a[i][j], visited[i][j])
    if a[i][j] == '.':
        return
    # bi = list(b[i])
    # bi[j] = '*'
    # b[i] = ''.join(bi)
    # for x in b:
    #     print(x)
    if a[i][j] == 'S':
        # dfs(i - 1, j, d + 1)
        dfs_prep(i, j + 1, d + 1, i, j)
        # dfs(i + 1, j, d + 1)
        # dfs(i, j - 1, d + 1)
    elif a[i][j] == '|':
        dfs_prep(i - 1, j, d + 1, i, j)
        dfs_prep(i + 1, j, d + 1, i, j)
    elif a[i][j] == '-':
        dfs_prep(i, j - 1, d + 1, i, j)
        dfs_prep(i, j + 1, d + 1, i, j)
    elif a[i][j] == 'L':
        dfs_prep(i, j + 1, d + 1, i, j)
        dfs_prep(i - 1, j, d + 1, i, j)
    elif a[i][j] == 'J':
        dfs_prep(i, j - 1, d + 1, i, j)
        dfs_prep(i - 1, j, d + 1, i, j)
    elif a[i][j] == '7':
        dfs_prep(i, j - 1, d + 1, i, j)
        dfs_prep(i + 1, j, d + 1, i, j)
    elif a[i][j] == 'F':
        dfs_prep(i ,j + 1, d + 1, i, j)
        dfs_prep(i + 1, j, d + 1, i, j)

for i in range(n):
    for j in range(m):
        # print(i, j, a[i][j])
        if a[i][j] == 'S':
            dfs(i, j, 0)

# for x in b:
#     print(x)
n = len(b)
m = len(b[0])
visited2 = []
for i in range(n):
    arr = []
    for j in range(m):
        arr.append(False)
    visited2.append(arr)
ans = 0

def dfs2(i ,j):
    # for x in b:
    #     print(x)
    global ans
    if i < 0 or j < 0 or i >= n or j >= m:
        return
    if visited2[i][j]:
        return
    visited2[i][j] = True
    if b[i][j] == '*':
        return
    if b[i][j] == '.' and i > 0 and j > 0 and i < n-1 and j < m-1:
        bi = list(b[i])
        bi[j] = '*'
        b[i] = ''.join(bi)
        ans += 1
    dfs2(i + 1, j)
    dfs2(i, j + 1)
    dfs2(i - 1, j)
    dfs2(i, j - 1)

b = b_ans.copy()
for x in b:
    print(x)

print('')
dfs2(1, 1)

for x in b:
    print(x)

ans = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        if b[i][j] == '.' and i%2==0 and j%2==0:
            ans += 1
print(ans)