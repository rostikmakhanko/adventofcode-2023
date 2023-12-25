def move(a, b, shift):
    if a[1] < b[0]:
        return [a]
    elif a[0] > b[1]:
        return [a]
    elif b[0] >= a[0] and b[1] <= a[1]:
        return [(a[0], b[0] - 1), (b[0] + shift, b[1] + shift), (b[1] + 1, a[1])]
    elif b[0] <= a[0] and b[1] < a[1]:
        return [(a[0] + shift, b[1] + shift), (b[1] + 1, a[1])]
    elif b[0] > a[0] and b[1] >= a[1]:
        return [(a[0], b[0] - 1), (b[0] + shift, a[1] + shift)]
    else:
        return [(a[0] + shift, a[1] + shift)]

def merge(a):
    a = sort(a)
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
            f = a[i][1]
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
# print(a)
na = len(a)
i = 2
while i < n:
    s = lines[i]
    # print(i, s)
    if s == '':
        i += 1
    elif s[0] >= '0' and s[0] <= '9':
        b = a.copy()
        while s != '':
            destination, source, size = s.split()
            destination = int(destination)
            source = int(source)
            size = int(size)
            # print(destination, source, size)
            for j in range(na):
                if a[j] >= source and a[j] <= source + size:
                    b[j] = destination + (a[j] - source)
            # print(a)
            i += 1
            if i >= n:
                break
            s = lines[i]
        a = b.copy()
    else:
        i += 1
print(min(a))
