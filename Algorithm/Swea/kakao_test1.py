def solution(board, moves):
    answer = 0
    doll  = []
    for i in range(len(moves)):
        j = 0
        while j < len(board):
            if board[j][moves[i] - 1] == 0:
                j += 1
            else:
                doll.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break
    k = 0
    while k < len(doll) - 1:
        if doll[k] == doll[k + 1]:
            doll.pop(k)
            doll.pop(k)
            k = 0
            answer += 2
            continue
        else:
            k += 1
    return answer

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[0,2,4,4,2],[0,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
