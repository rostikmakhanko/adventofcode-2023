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
ans = 0
for s in a:
    ans += get_hash(s)
print(ans)