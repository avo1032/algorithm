def solution(arr):
    arrDiff = len(arr) - len(arr[0])
    if(arrDiff > 0):
        for i in range(arrDiff):
            for i in range(len(arr)):
                arr[i].append(0)
    else:
        addArr = [0] * (len(arr) + (-arrDiff))
        for i in range(-arrDiff):
            arr.append(addArr)
    return arr

solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]])