import sys

N, M = list(map(int, sys.stdin.readline().split()))

N_doc = {}
ans_list = []
for _ in range(N):
    N_doc[sys.stdin.readline().rstrip()] = 1


for _ in range(M):
    M_target = sys.stdin.readline().rstrip()
    if M_target in N_doc:
        ans_list.append(M_target)

print(len(ans_list))
ans_list.sort()
for i, target in enumerate(ans_list):
    print(target)
