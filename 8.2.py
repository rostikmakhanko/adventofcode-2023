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
    # print(cur, left, right)
    g[cur] = (left, right)
s = s * 100
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
    # print(z)
    sim[nodes[i]] = (cur, z)
nn = 16
shift = len(s)
while nn:
    new_sim = {}
    nn -= 1
    shift *= 2
    for i in range(n-2):
        cur1 = nodes[i]
        next1 = sim[cur][0]
        zetky = sim[cur][1]
        # print(zetky)
        shift_zetky = list(map(lambda x: x + shift, zetky))
        new_sim[cur1] = (next1, zetky + shift_zetky)
    sim = new_sim.copy()

start_n = len(start)
ans = 0
# print(start)
kk = 0
for c in s:
    ans += 1
    d = -1
    if c == 'L':
        d = 0
    else:
        d = 1
    k = 0
    # print(start)
    for i in range(start_n):
        start[i] = g[start[i]][d]
        if start[i][2] == 'Z':
            # print(start[0])
            k += 1
    # print(start)
    kk = max(k, kk)
    if k == start_n:
        print(ans)
        break

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

iters = int(1e6+5)
print('shift', shift)
shift1 = shift
shift = 0
while iters:
    shift += shift1
    print(shift)
    zp_arr = []
    start_new = []
    for i in range(start_n):
        cur = start[i]
        zp_a = list(map(lambda x: x + shift, sim[cur][1]))
        zp_arr.append(zp_a)
        start_new.append(sim[cur][0])
    # print(zp_arr)
    if is_cool(zp_arr):
        # print(zp_arr)
        print('|||', iters)
        break
    start = start_new.copy()
    iters -= 1
print(ans)
# print(kk)