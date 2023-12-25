import sys
sys.setrecursionlimit(100000)

lines = list(open('19.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

workflows = []
ratings = []
f = False
for line in lines:
    if not f:
        if line == '':
            f = True
            continue
        workflows.append(line)
    else:
        ratings.append(line)

# print(workflows, ratings)

w = {}
for workflow in workflows:
    value, s = workflow.split('{')
    s = s.split('}')[0]
    a = s.split(',')
    steps = []
    for x in a:
        if '<' in x:
            pos = x.find('<')
            from1 = 0
            to1 = int(x[2:x.find(':')])
            next1 = x[x.find(':')+1:]
            add1 = (x[0], (from1, to1), next1)
            steps.append(add1)
        elif '>' in x:
            pos = x.find('>')
            from1 = int(x[2:x.find(':')])
            to1 = int(1e9+7)
            next1 = x[x.find(':')+1:]
            add1 = (x[0], (from1, to1), next1)
            steps.append(add1)
        else:
            from1 = 0
            to1 = int(1e9+7)
            next1 = x
            add1 = ('', (from1, to1), next1)
            print(add1)
            steps.append(add1)
    w[value] = steps
    # print(value, steps)

def go(r_set, value):
    if value == 'R':
        return False
    if value == 'A':
        return True
    conditions = w[value]
    for c in conditions:
        # print(c)
        r1 = c[0]
        from1 = c[1][0]
        to1 = c[1][1]
        next1 = c[2]
        # print(r1, from1, to1, next1)
        # print(r_set)
        if r1 == '':
            return go(r_set, next1)
        if r_set[r1] > from1 and r_set[r1] < to1:
            return go(r_set, next1)
        # print(value1)
    
ans = 0
for rating in ratings:
    r = rating[1:-1].split(',')
    # print(rating[1:-1].split(','))
    r_set = {'': 0}
    ans1 = 0
    for r1 in r:
        # print(r1[0], r1[2:])
        r_set[r1[0]] = int(r1[2:])
        ans1 += int(r1[2:])
    if go(r_set, "in"):
        ans += ans1
print(ans)
