import sys
sys.setrecursionlimit(100000)

lines = list(open('18.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

i1 = 0
j1 = 0
min_i = 0
min_j = 0
max_i = 0
max_j = 0
moves = []
for line in lines:
    a = line.split(' ')
    t1 = a[0]
    x1 = int(a[1])
    moves.append((t1, x1))
    if t1 == 'R':
        j1 += x1
    elif t1 == 'L':
        j1 -= x1
    elif t1 == 'U':
        i1 -= x1
    elif t1 == 'D':
        i1 += x1
    min_i = min(min_i, i1)
    min_j = min(min_j, j1)
    max_i = max(max_i, i1)
    max_j = max(max_j, j1)
n = max_i - min_i + 1
m = max_j - min_j + 1
i1 = abs(min_i)
j1 = abs(min_j)
board = []
for i in range(n):
    x = []
    for j in range(m):
        x.append('.')
    board.append(x)
board[i1][j1] = '#'
for move in moves:
    t1 = move[0]
    x1 = move[1]
    if t1 == 'R':
        for j in range(j1+1, j1+x1+1):
            board[i1][j] = '#'
        j1 += x1
    elif t1 == 'L':
        for j in range(j1-1, j1-x1-1, -1):
            board[i1][j] = '#'
        j1 -= x1
    elif t1 == 'U':
        for i in range(i1-1, i1-x1-1, -1):
            board[i][j1] = '#'
        i1 -= x1
    elif t1 == 'D':
        for i in range(i1+1, i1+x1+1):
            board[i][j1] = '#'
        i1 += x1
for line in board:
    print(''.join(line))

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    if board[i][j] == '#':
        return
    board[i][j] = '#'
    dfs(i-1, j)
    dfs(i, j-1)
    dfs(i+1, j)
    dfs(i,j+1)

dfs(1, 168)
ans = 0
for line in board:
    for c in line:
        if c == '#':
            ans += 1
print(ans)