lines = list(open('14.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

def get_sum(n):
    return n*(n+1)//2

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