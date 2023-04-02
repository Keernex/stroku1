listrandom = list(input().split())
l = []
for i in listrandom:
    if i not in l:
        l.append(i)
print(l)