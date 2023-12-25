def get_hash(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

lines = list(open('15.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
a = lines[0].split(',')
ans = []
kk = []
for i in range(256):
    ans.append({})
    kk.append(0)
for s in a:
    # ans += get_hash(s)
    arr = s.split('=')
    if len(arr) > 1:
        s1 = arr[0]
        f1 = int(arr[1])
        h1 = get_hash(s1)
        if s1 in ans[h1]:
            k1 = ans[h1][s1][1]
            ans[h1][s1] = (f1, k1)
        else:
            kk[h1] += 1
            ans[h1][s1] = (f1, kk[h1])
    else:
        arr = s.split('-')
        s1 = arr[0]
        h1 = get_hash(s1)
        if s1 in ans[h1]:
            del ans[h1][s1]
answer = 0
for i in range(256):
    b = []
    for key in ans[i]:
        print(key, ans[i][key])
        b.append((ans[i][key][1], ans[i][key][0]))
    b.sort()
    if len(b) > 0:
        print(b)
    for j in range(len(b)):
        print(i+1, j+1, b[j][1], b[j][0])
        answer += (i+1)*(j+1)*b[j][1]
        # print(answer)
print(answer)