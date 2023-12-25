# a = [7, 15, 30]
# b = [9, 40, 200]
a = [50748685]
b = [242101716911252]
ans = 1
for i in range(len(a)):
    x = a[i]
    k = 0
    for j in range(x):
        speed = j
        time = x - j
        if speed * time > b[i]:
            k += 1
    ans *= k
print(ans)