data = [int(input()) for _ in range(3)]

doc = {"0": 0, "1": 0, "2": 0,"3": 0, "4": 0, "5": 0,"6": 0, "7": 0, "8": 0,"9": 0}
num = 1
for i in data:
    num = num * i

for j in (list(str(num))):
    doc[j] += 1

for z in range(10):
    print(doc[str(z)])