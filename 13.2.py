def get_ans(a):
    n = len(a)
    m = len(a[0])
    ans = 0
    for i in range(n-1):
        i1 = i
        i2 = i + 1
        while i1 >= 0 and i2 < n:
            # print(i1, i2)
            if a[i1] != a[i2]:
                break
            else:
                i1 -= 1
                i2 += 1
        if i1 == -1 or i2 == n:
            ans = max(ans, i+1)
    return ans

def get_a_traversed(a):
    n = len(a)
    m = len(a[0])
    b = []
    for j in range(m):
        s = ""
        for i in range(n-1,-1,-1):
            s += a[i][j]
        b.append(s)
    return b

lines = list(open('13.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

a = []
ans = 0
lines.append("")
for line in lines:
    if line == "":
        ans_old = max(get_ans(get_a_traversed(a)), get_ans(a) * 100)
        ans_new = ans_old
        n = len(a)
        m = len(a[0])
        for i in range(n):
            for j in range(m):
                b = []
                for i1 in range(n):
                    b.append(a[i1])
                print(b[i])
                if b[i][j] == '.':
                    b[i] = b[i][:j] + '#' + b[i][j+1:]
                else:
                    b[i] = b[i][:j] + '.' + b[i][j+1:]
                print(b[i])
                # print(b)
                x = get_ans(get_a_traversed(b))
                y = get_ans(b) * 100
                ans1 = max(get_ans(get_a_traversed(b)), get_ans(b) * 100)
                if (x != ans_old and x > 0) and (y != ans_old and y > 0):
                    print('both', i, j, x, y)
                if x != ans_old and x > 0:
                    ans_new = x
                    break
                if y != ans_old and y > 0:
                    ans_new = y
                    break
            if ans_new != ans_old:
                break
        ans += ans_new
        a = []
        # print(ans)
    else:
        a.append(line)
print(ans)