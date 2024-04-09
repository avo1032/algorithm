# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# max_num = 0

# for i in range(a[0]-2):
#     for j in range(i + 1, a[0]):
#         for z in range(i + 2, a[0]):
#             sum = b[i] + b[j] + b[z]
#             if sum >= max_num and sum <= a[1]:
#                 max_num = sum
#             if max_num == a[1]:
#                 break
#         if max_num == a[1]:
#             break
#     if max_num == a[1]:
#         break

# print(max_num)

a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_num = 0

for i in range(a[0] - 2):
    for j in range(i + 1, a[0] - 1):
        for z in range(j + 1, a[0]):
            current_sum = b[i] + b[j] + b[z]
            if current_sum > max_num and current_sum <= a[1]:
                max_num = current_sum
            if max_num == a[1]:
                print(max_num)
                exit(0)

print(max_num)