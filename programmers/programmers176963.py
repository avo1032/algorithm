def solution(name, yearning, photo):
    nameDic = {}
    for k in range(len(name)):
        nameDic[name[k]] = yearning[k]
    answer = [0] * len(photo)
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            answer[i] += nameDic.get(photo[i][j], 0)
    return answer


solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
# 0으로 채워진 배열 만들기
# 순회하며 배열에 값 올리기