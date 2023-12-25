def move(a, b, shift):
    if a[1] < b[0]:
        return [a]
    elif a[0] > b[1]:
        return [a]
    elif b[0] > a[0] and b[1] < a[1]:
        return [(a[0], b[0] - 1), (b[0] + shift, b[1] + shift), (b[1] + 1, a[1])]
    elif b[0] <= a[0] and b[1] < a[1]:
        return [(a[0] + shift, b[1] + shift), (b[1] + 1, a[1])]
    elif b[0] > a[0] and b[1] >= a[1]:
        return [(a[0], b[0] - 1), (b[0] + shift, a[1] + shift)]
    else:
        return [(a[0] + shift, a[1] + shift)]

def move_new(a, b, shift):
    if a[1] < b[0]:
        return []
    elif a[0] > b[1]:
        return []
    elif b[0] > a[0] and b[1] < a[1]:
        return [(b[0] + shift, b[1] + shift)]
    elif b[0] <= a[0] and b[1] < a[1]:
        return [(a[0] + shift, b[1] + shift)]
    elif b[0] > a[0] and b[1] >= a[1]:
        return [(b[0] + shift, a[1] + shift)]
    else:
        return [(a[0] + shift, a[1] + shift)]

def move_old(a, b, shift):
    if a[1] < b[0]:
        return [a]
    elif a[0] > b[1]:
        return [a]
    elif b[0] > a[0] and b[1] < a[1]:
        return [(a[0], b[0] - 1), (b[1] + 1, a[1])]
    elif b[0] <= a[0] and b[1] < a[1]:
        return [(b[1] + 1, a[1])]
    elif b[0] > a[0] and b[1] >= a[1]:
        return [(a[0], b[0] - 1)]
    else:
        return []

def merge(a):
    a.sort()
    n = len(a)
    if n == 0:
        return a
    i = 0
    s = a[0][0]
    f = a[0][1]
    i = 1
    ans = []
    while i < n:
        if a[i][0] <= f:
            f = max(f, a[i][1])
        else:
            ans.append((s, f))
            s = a[i][0]
            f = a[i][1]
        i += 1
    ans.append((s, f))
    return ans

lines = list(open('5.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
n = len(lines)
p = lines[0].find(':') + 2
sa = lines[0][p:]
a = sa.split()
for i in range(len(a)):
    a[i] = int(a[i])
a1 = []
for i in range(0, len(a), 2):
    a1.append((a[i], a[i] + a[i+1] - 1))
n1 = len(a1)
# print(a)
na = len(a)
i = 2
# print(a1)
# print(a1)
while i < n:
    s = lines[i]
    # print(i, s)
    if s == '':
        i += 1
    elif s[0] >= '0' and s[0] <= '9':
        b1 = []
        f = []
        a1_left = a1.copy()
        for x in b1:
            f.append(False)
        while s != '':
            destination, source, size = s.split()
            destination = int(destination)
            source = int(source)
            size = int(size)
            source_range = (source, source + size - 1)
            shift = destination - source
            # print(destination, source, size)
            b1_left = []
            for j in range(len(a1_left)):
                # print(i)
                # print(a1[j], source_range, shift)
                # print(move(a1[j], source_range, shift))
                b1 = b1 + move_new(a1_left[j], source_range, shift)
                b1_left = b1_left + move_old(a1_left[j], source_range, shift)
            a1_left = merge(b1_left)
            # print(a)
            i += 1
            if i >= n:
                break
            s = lines[i]
        # print(b1, merge(b1))
        a1 = merge(b1 + a1_left)
        # print(a1)
    else:
        i += 1
ans = a1[0][0]
for x in a1:
    ans = min(ans, x[0])
print(ans)
