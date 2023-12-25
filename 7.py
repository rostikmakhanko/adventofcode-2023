from functools import cmp_to_key

cards = "AKQJT98765432"

lines = list(open('7.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

def get_rank(s):
    if s[1] == s[0] and s[2] == s[0] and s[3] == s[0] and s[4] == s[0]:
        return 1
    a = []
    for c in s:
        k = s.count(c)
        a.append((k, c))
    a.sort()
    a.reverse()
    # print(a)
    if a[0][0] == 4:
        return 2
    if a[0][0] == 3 and a[3][0] == 2:
        return 3
    if a[0][0] == 3:
        return 4
    if a[0][0] == 2 and a[2][0] == 2:
        return 5
    if a[0][0] == 2:
        return 6
    return 7
    


def comp_s(a1, b1):
    a = a1[0]
    b = b1[0]
    # print(a, b)
    ra = get_rank(a)
    rb = get_rank(b)
    # print(ra, rb)
    if ra < rb:
        # print(-1)
        return -1
    elif ra > rb:
        # print(1)
        return 1
    for i in range(5):
        a1p = cards.find(a[i])
        b1p = cards.find(b[i])
        # print(a[i], b[i])
        # print(a1p, b1p)
        if a1p < b1p:
            # print(-1)
            return -1
        elif a1p > b1p:
            # print(1)
            return 1
    # print(0)
    return 0

p = []
for line in lines:
    a1, b1 = line.split()
    p.append((a1, int(b1)))
# print(p)
p = sorted(p, key=cmp_to_key(comp_s))
p.reverse()
i = 0
ans = 0 
for x in p:
    i += 1
    ans += i * x[1]
print(ans)