def solution(id_list, report, k):
    answer = []
    report_doc = { }
    result_doc = { }
    for i in id_list:
        report_doc[i] = []
        result_doc[i] = 0
    for j in report:
        n, z = j.split()
        if not n in report_doc[z]:
            report_doc[z].append(n)
    for target, mans in report_doc.items():
        if len(mans) >= k:
            for f in mans:
                result_doc[f] += 1
    answer = list(result_doc.values())
    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)

# report_doc 에 누가 몇번 신고당했는지
# report_list에
# doc = {
#     "muzi": [],
#     "frodo": ["muzi", "neo"]
# }
# for key, value in doc.items():
#     print(key)
#     print(value)