N = int(input())
K = list(map(int, input().split()))
M = int(input())
J = list(map(int, input().split()))

numbers_doc = { }
result_list = []
for i in K:
    if i in numbers_doc:
        numbers_doc[i] += 1
    else:
        numbers_doc[i] = 1

for j in J:
    if j in numbers_doc:
        result_list.append(str(numbers_doc[j]))
    else:
        result_list.append('0')

print(' '.join(result_list))