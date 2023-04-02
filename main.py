q = input()
q=q+" "
l=[]
r=""
for i in range(len(q)):
  if q[i] == " " and q[i-1] != " ":
    l.append(r)
    r=""
  else:
    r+=q[i]
print(*l[::-1])