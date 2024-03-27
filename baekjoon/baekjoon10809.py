n = list(input())
result = [-1] * 26

for i, alpha in enumerate(n):
    index = ord(alpha) - ord('a')
    if result[index] == -1:
        result[index] = i

print(' '.join(str(s) for s in result))