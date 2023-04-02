q = input()
w = 0
e = 0
for i in q:
  if i.isalpha() == True:
    w += 1
  elif i.isdigit() == True:
    e += 1
print(f"букви: {w}; цифри: {e};")
