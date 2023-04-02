q = list(input('Введіть ряд строк через пробіл: ').split())
w = input("пошук: ")
e = input("заміна: ")
l=[]
for i in q:
  if w == i:
    l.append(e)
  else:
    l.append(i)
print(*l)
