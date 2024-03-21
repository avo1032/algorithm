def solution(boards, moves):
    answer = 0
    stack = []

    for move in moves:
        for i, board in enumerate(boards):
            # if not board[move-1] == 0:
                # print('move-1 :: ',move-1)
                # print(board[move-1])
            if board[move-1] == 0:
                continue
            if stack and stack[-1] == board[move-1]:
                stack.pop()
                board[move-1] = 0
                answer += 2
                break
            else:
                stack.append(board[move-1])
                # print(stack)
                board[move-1] = 0
                break
    print(answer)
    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])

# 4 3 1 1 3 2 0 4
# for move in enumerate([1, 2, 3,4 ]):
#     print(move)


# move에 해당하는 인형 뽑기
# stack에 있는 인형과 같으면 pop, answer += 2
# stack에 있는 인형과 다르면 append