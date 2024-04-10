import sys

n = int(sys.stdin.readline())

for i in range(n):
    words = sys.stdin.readline().rstrip().split()
    reversed_words = []
    
    while len(words) > 0:
        reversed_words.append(words.pop())
    
    print(f"Case #{i+1}: {' '.join(reversed_words)}")