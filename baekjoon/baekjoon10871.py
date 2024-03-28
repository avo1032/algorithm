n = list(map(int, input().split()))
data = list(map(int, input().split()))

answer = ""

for i in data:
    if i < n[1]:
        if answer == "":
            answer += str(i)
        else:
            answer += " "+str(i)

print(answer)
