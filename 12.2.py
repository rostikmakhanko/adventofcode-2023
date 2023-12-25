lines = list(open('12.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

def check(s, a):
    sn = len(s)
    an = len(a)
    k = 0
    j = 0
    for i in range(sn):
        if s[i] == '#':
            k += 1
        else:
            if k > 0:
                if j >= an:
                    return False
                if a[j] != k:
                    return False
                j += 1
                k = 0
    if k > 0:
        if j >= an:
            return False
        if a[j] != k:
            return False
        j += 1
        k = 0
    if j == an:
        return True
    else:
        return False

def calc(s, i, a):
    if i == len(s):
        # print(s)
        return 1 if check(s, a) else 0
    ans = 0
    ans += calc(s, i+1, a)
    if s[i] == '?':
        s_arr = list(s)
        s_arr[i] = '#'
        s_new = ''.join(s_arr)
        ans += calc(s_new, i+1, a)
    return ans

answer = 0
for line in lines:
    s = line.split(' ')[0]*5
    a = line.split(' ')[1]
    a = a + ',' + a + ',' + a + ',' + a + ',' + a
    a = a.split(',')
    a = list(map(lambda x: int(x), a))
    print(s, a)
    # print(calc(s, 0, a))
    answer += calc(s, 0, a)
    print(line)
print(answer)