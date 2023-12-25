def is_cool(a):
    n = len(a)
    for x in a[0]:
        k = 0
        for arr in a:
            if x in arr:
                k += 1
        if k == n:
            print('annnns', x)
            return True
    return False

lines = list(open('8.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

n = len(lines)
s = lines[0]
g = {}
start = []
nodes = []
for i in range(2, n):
    s1 = lines[i]
    cur = s1[:3]
    nodes.append(cur)
    if cur[2] == 'A':
        start.append(cur)
    left = s1[7:10]
    right = s1[12:15]
    g[cur] = (left, right)
s = s
ns = len(s)
sim = {}
for i in range(n - 2):
    j = 0
    cur = nodes[i]
    z = []
    for c in s:
        j += 1
        d = -1
        if c == 'L':
            d = 0
        else:
            d = 1
        cur = g[cur][d]
        if cur[2] == 'Z':
            z.append(j)
    sim[nodes[i]] = (cur, z)

print(start)
ans = []
for s_start in start:
    visited = {}
    cur = s_start
    j = 0
    while not (cur in visited):
        print(cur)
        visited[cur] = j
        cur = sim[cur][0]
        j += 1
        if cur[2] == "Z":
            print('Z:', j)
            ans.append(j)
    print(j, cur, visited[cur])
ans1 = len(s)
for x in ans:
    ans1 *= x
print(ans1)
# print(n-2)
# shift = ns
# for i in range(100):
#     kk = 0
#     kkk = 0
#     sim1 = {}
#     check = []
#     for j in range(n-2):
#         # print(j)
#         from1 = nodes[j]
#         to1 = sim[from1][0]
#         to2 = sim[to1][0]
#         z1 = sim[from1][1]
#         add_new = sim[to2][1]
#         add_new = list(map(lambda x: x + shift, add_new))
#         sz_new = sim[to1][1] + add_new
#         sim1[from1] = (sim[to2][0], sz_new)
#         # print(len(from1))
#         # print(from1, to1, to2)
#         # print(from1, sim[to1][0], sim[to1][1])
#         # print(from1[2] == 'A')
#         if from1[2] == 'A' and sim[to2][0][2] != 'Z':
#             kk += 1
#             # print(sim[to1][1])
#             if len(sz_new) > 0:
#                 kkk += 1
#                 check.append(sz_new)
#                 # print('HASSS', i)
#         elif from1[2] == 'A':
#             print('GOOD')
#         else:
#             # print('MED')
#             pass
#     if kk == 0:
#         print('ANS:', i)
#     if kkk >= 6:
#         print('ALL SIX', kkk, i)
#         print('is good', is_cool(check))
#     sim = sim1.copy()
#     shift *= 2