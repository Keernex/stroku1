#q = list(input('Введіть ряд строк через пробіл: ').split())
l=input()
l=l+" "
q=[]
r=""
for i in range(len(l)):
  if l[i]==" " and l[i-1]!=" ":
    q.append(r)
    r=""
  elif l[i]=="." or l[i]=="," or l[i]=="!" or l[i]=="?":
    r+=""
  else:
    r+=l[i]

w = input()
e = 0
for i in q:
  if w == i:
    e += 1
print(e)
