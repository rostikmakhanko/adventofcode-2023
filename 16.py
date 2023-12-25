import sys  
sys.setrecursionlimit(100000)

lines = list(open('16.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
print(lines[0])

visited = []
for line in lines:
    x = []
    for c in line:
        x.append({})
    visited.append(x)

n = len(lines)
m = len(lines[i])

def dfs(i, j, d):
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    if d in visited[i][j]:
        return
    # print(i, j, lines[i][j])
    visited[i][j][d] = True
    if lines[i][j] == '.':
        if d == 'R':
            print('go right')
            dfs(i, j+1, d)
        elif d == 'L':
            dfs(i, j-1, d)
        elif d == 'D':
            dfs(i+1, j, d)
        elif d == 'U':
            dfs(i-1, j, d)
    elif lines[i][j] == '/':
        if d == 'R':
            dfs(i-1, j, 'U')
        elif d == 'L':
            dfs(i+1, j, 'D')
        elif d == 'D':
            dfs(i, j-1, 'L')
        elif d == 'U':
            dfs(i, j+1, 'R')
    elif lines[i][j] == '\\':
        if d == 'R':
            dfs(i+1, j, 'D')
        elif d == 'L':
            dfs(i-1, j, 'U')
        elif d == 'D':
            dfs(i, j+1, 'R')
        elif d == 'U':
            dfs(i, j-1, 'L')
    elif lines[i][j] == '-':
        if d == 'R':
            dfs(i, j+1, 'R')
        elif d == 'L':
            dfs(i, j-1, 'L')
        elif d == 'D':
            dfs(i, j-1, 'L')
            dfs(i, j+1, 'R')
        elif d == 'U':
            dfs(i, j-1, 'L')
            dfs(i, j+1, 'R')
    elif lines[i][j] == '|':
        if d == 'R':
            dfs(i-1, j, 'U')
            dfs(i+1, j, 'D')
        elif d == 'L':
            dfs(i-1, j, 'U')
            dfs(i+1, j, 'D')
        elif d == 'D':
            dfs(i+1, j, 'D')
        elif d == 'U':
            dfs(i-1, j, 'U')

default_visited = visited.copy()
print(default_visited)

answer = 0
for ii in range(n):
    visited = []
    for line in lines:
        x = []
        for c in line:
            x.append({})
        visited.append(x)
    dfs(ii, 0, 'R')
    ans = 0
    for i in range(n):
        for j in range(m):
            if 'R' in visited[i][j] or 'L' in visited[i][j] or 'U' in visited[i][j] or 'D' in visited[i][j]:
                ans += 1
    answer = max(ans, answer)
for ii in range(n):
    visited = []
    for line in lines:
        x = []
        for c in line:
            x.append({})
        visited.append(x)
    dfs(ii, m-1, 'L')
    ans = 0
    for i in range(n):
        for j in range(m):
            if 'R' in visited[i][j] or 'L' in visited[i][j] or 'U' in visited[i][j] or 'D' in visited[i][j]:
                ans += 1
    answer = max(ans, answer)
for jj in range(m):
    visited = []
    for line in lines:
        x = []
        for c in line:
            x.append({})
        visited.append(x)
    dfs(0, jj, 'D')
    ans = 0
    for i in range(n):
        for j in range(m):
            if 'R' in visited[i][j] or 'L' in visited[i][j] or 'U' in visited[i][j] or 'D' in visited[i][j]:
                ans += 1
    answer = max(ans, answer)
for jj in range(m):
    visited = []
    for line in lines:
        x = []
        for c in line:
            x.append({})
        visited.append(x)
    dfs(n-1, jj, 'U')
    ans = 0
    for i in range(n):
        for j in range(m):
            if 'R' in visited[i][j] or 'L' in visited[i][j] or 'U' in visited[i][j] or 'D' in visited[i][j]:
                ans += 1
    answer = max(ans, answer)
print(answer)