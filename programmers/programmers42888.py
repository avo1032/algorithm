def solution(record):
    answer = []
    result = []
    uidDoc = { }
    for i in record:
        splitRecord = i.split(" ")
        if splitRecord[0] == "Enter" or splitRecord[0] == "Change":
            uidDoc[splitRecord[1]] = splitRecord[2]
        
        if splitRecord[0] == "Enter":
            answer.append(["Enter", splitRecord[1]])

        if splitRecord[0] == "Leave":
            answer.append(["Leave", splitRecord[1]])
    
    for j in answer:
        if j[0] == "Enter":
            result.append(uidDoc[j[1]] + "님이 들어왔습니다.")
        if j[0] == "Leave":
            result.append(uidDoc[j[1]] + "님이 나갔습니다.")
    return result

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])