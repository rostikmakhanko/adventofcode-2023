digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def  get_calibrattion_number(s):
    first = 10
    last = -1
    n = len(digits)
    fx = int(1e9+7)
    lx = -1
    for i in range(n):
        x = s.find(digits[i])
        if x < fx and x >= 0:
            fx = x
            first = i + 1
    for i in range(n):
        x = s.rfind(digits[i])
        if x > lx and x >= 0:
            lx = x
            last = i + 1
    n1 = len(s)
    for i in range(n1):
        if s[i] >= '0' and s[i] <= '9':
            first1 = int(s[i])
            if i < fx:
                first = first1
            break
    for i in range(n1 - 1, -1, -1):
        if s[i] >= '0' and s[i] <= '9':
            last1 = int(s[i])
            if i > lx:
                last = last1
            break
    return first*10 + last

lines = tuple(open('1.txt', 'r'))
ans = 0
for line in lines:
    print(get_calibrattion_number(line))
    ans += get_calibrattion_number(line)
print(ans)