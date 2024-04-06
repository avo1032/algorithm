import sys

while True:
    nums = sys.stdin.readline().strip()
    if nums == "0 0 0":
        break
    sides = list(map(int, nums.split()))
    sides.sort()
    a, b, c = sides
    if a * a + b * b == c * c:
        print("right")
    else:
        print("wrong")