import sys
sys.setrecursionlimit(100000)

lines = list(open('24.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
p = []
v = []
for line in lines:
    p1, v1 = line.split('@')
    p1 = p1.split(', ')
    v1 = v1.split(', ')
    p.append((int(p1[0]), int(p1[1]), int(p1[2])))
    v.append((int(v1[0]), int(v1[1]), int(v1[2])))
n = len(p)

def get_cross(k1, b1, k2, b2):
    if k1 == k2:
        return None
    # y = k1*x+b1
    # y = k2*x+b2
    # k1*x+b1=k2*x+b2
    # x*(k1-k2)=b2-b1
    # x = (b2-b1)/(k1-k2)
    x = (b2-b1)/(k1-k2)
    y = k1*x+b1
    return (x, y)

def get_k(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def get_b(x1, y1, k):
    return y1-k*x1

ans = 0
for i in range(n):
    for j in range(i+1, n):
        p1 = p[i]
        p2 = p[j]
        v1 = v[i]
        v2 = v[j]
        k1 = get_k(p1[0], p1[1], p1[0]+v1[0], p1[1]+v1[1])
        b1 = get_b(p1[0], p1[1], k1)
        # print('y=', k1, '*x+', b1)
        k2 = get_k(p2[0], p2[1], p2[0]+v2[0], p2[1]+v2[1])
        b2 = get_b(p2[0], p2[1], k2)
        # print('y=', k2, '*x+', b2)
        pp = get_cross(k1, b1, k2, b2)
        # print(i, j, pp)
        if pp:
            if pp[0] >= 200000000000000 and pp[0] <= 400000000000000 and pp[1] >= 200000000000000 and pp[1] <= 400000000000000:
                if v1[0] > 0 and pp[0] < p1[0]:
                    continue
                if v2[0] > 0 and pp[0] < p2[0]:
                    continue
                if v1[0] < 0 and pp[0] > p1[0]:
                    continue
                if v2[0] < 0 and pp[0] > p2[0]:
                    continue
                ans += 1
print(ans)
