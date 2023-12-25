import sys
sys.setrecursionlimit(100000)

lines = list(open('25.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

love = {'': 0}
names = []
edges = []
g = {'123': {'321'}}
for line in lines:
    a, b = line.split(': ')
    b = b.split(' ')
    if a not in love:
        names.append(a)
        love[a] = 0
    for x in b:
        edges.append((a, x))
        if x not in love:
            names.append(x)
            love[x] = 1
            g[x] = {''}
            g[x].add(a)
        else:
            love[x] = love[x]+1
        love[a] = love[a]+1
for e1 in edges:
    for e2 in edges:
        q = 1

# vph - tjz
# jhq - zkt
# pgt - lnr

bad = [('vph', 'tjz'), ('jhq', 'zkt'), ('pgt', 'lnr')]
g1 = {'123': []}
visited = {'123': False}
for name in names:
    visited[name] = False
    g1[name] = []
for e in edges:
    print(e)
    if e not in bad and (e[1], e[0]) not in bad:
        g1[e[0]].append(e[1])
        g1[e[1]].append(e[0])

k1 = 0
k2 = len(names)
def dfs(v):
    global k1
    global k2
    k1 += 1
    k2 -= 1
    visited[v] = True
    for neighbor in g1[v]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs('vph')
print(k1*k2)
