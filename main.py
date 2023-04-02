q = list(input('Введіть ряд строк через пробіл: ').split())
w = input()
e = 0
for i in q:
  if w == i:
    e += 1
print(e)
