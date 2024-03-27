data = list(map(int, input().split()))

data2 = data.copy()
data2.pop(0)

if data2[0] > data[0]:
    for index, num in enumerate(data2):
        if num < data[index]:
            print('mixed')
            break
    else:
        print("ascending")

if data2[0] < data[0]:
    for index, num in enumerate(data2):
        if num > data[index]:
            print('mixed')
            break
    else:
        print("descending")