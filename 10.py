import sys
sys.setrecursionlimit(1000000)

lines = list(open('10.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
n = len(lines)
m = len(lines[i])
a = []
a.append('.' * (n+2))
for line in lines:
    a.append('.' + line + '.')
a.append('.' * (n+2))
n += 2
m += 2
visited = []
for i in range(n):
    arr = []
    for j in range(m):
        arr.append(False)
    visited.append(arr)

def dfs(i, j, d):
    # print(a[i][j], visited[i][j])
    if visited[i][j]:
        if a[i][j] == 'S':
            if d%2 == 0:
                print(d//2)
            else:
                print(d//2 + 1)
        return
    visited[i][j] = True
    if a[i][j] == '.':
        return
    if a[i][j] == 'S':
        # dfs(i - 1, j, d + 1)
        dfs(i, j + 1, d + 1)
        dfs(i + 1, j, d + 1)
        # dfs(i, j - 1, d + 1)
    elif a[i][j] == '|':
        dfs(i - 1, j, d + 1)
        dfs(i + 1, j, d + 1)
    elif a[i][j] == '-':
        dfs(i, j - 1, d + 1)
        dfs(i, j + 1, d + 1)
    elif a[i][j] == 'L':
        dfs(i, j + 1, d + 1)
        dfs(i - 1, j, d + 1)
    elif a[i][j] == 'J':
        dfs(i, j - 1, d + 1)
        dfs(i - 1, j, d + 1)
    elif a[i][j] == '7':
        dfs(i, j - 1, d + 1)
        dfs(i + 1, j, d + 1)
    elif a[i][j] == 'F':
        dfs(i ,j + 1, d + 1)
        dfs(i + 1, j, d + 1)

for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            dfs(i, j, 0)
