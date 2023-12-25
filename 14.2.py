lines = list(open('14.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

def get_sum(n):
    return n*(n+1)//2

def get_a_traversed(a):
    n = len(a)
    m = len(a[0])
    b = []
    for j in range(m):
        s = ""
        for i in range(n-1, -1, -1):
            s += a[i][j]
        b.append(s)
    return b

# a = []
# for line in lines:
#     a.append(line.split(''))

def get_a_north(a1):    
    n = len(a1)
    m = len(a1[0])
    b = []
    a = []
    for i in range(n):
        a.append(list(a1[i]))
    for j in range(m):
        s = ""
        for i in range(n):
            if a[i][j] == 'O':
                i1 = i - 1
                while i1 >= 0:
                    if a[i1][j] != '.':
                        break
                    i1 -= 1
                if i1+1 != i:
                    a[i1+1][j] = 'O'
                    a[i][j] = '.'
        b.append(s)
    return a

nn = 1
a = lines.copy()
print(a)
while nn:
    nn -= 1
    nn1 = 4
    while nn1:
        nn1 -= 1
        a = get_a_north(a)
        a = get_a_traversed(a)

print(a)

lines = a.copy()
n = len(lines)
m = len(lines[0])
ans = 0
for j in range(m):
    k = 0
    start = n
    start_i = n
    i = 0
    while i < n:
        start_i -= 1
        if lines[i][j] == 'O':
            k += 1
        elif lines[i][j] == '#':
            if k > 0:
                finish = start - k + 1
                ans += get_sum(start) - get_sum(finish - 1)
                k = 0
                # print('0', start, finish, j, i, ans)
            start = start_i
        i += 1
    if k > 0:
        finish = start - k + 1
        ans += get_sum(start) - get_sum(finish - 1)
        # print('1', start, finish, j, i, ans)
print(ans)