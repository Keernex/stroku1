q = list(input().split())
elem = ""
e = 0
for i in q:
  if q.count(i) > e:
    e = q.count(i)
    elem = i
print(elem)