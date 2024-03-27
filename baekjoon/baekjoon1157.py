words = list(input())
doc = { }
for i in words:
    if doc.get(i.upper()) == None:
        doc[i.upper()] = 1
    else:
        doc[i.upper()] += 1

d1 = list(sorted(doc.items(), key=lambda x: x[1], reverse=True))

if len(d1) > 1:
    if d1[0][1] == d1[1][1]:
        print("?")
    else:
        print(d1[0][0])
else:
    print(d1[0][0])