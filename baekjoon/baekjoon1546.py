n = int(input())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
top = numbers[0]

print(sum(numbers) / (n * top) * 100)