def solution(board, moves):
    stack = []
    count = 0
    
    for m in moves:
        m -= 1
        for i in range(len(board)):
            doll = board[i][m]
            if doll != 0:
                board[i][m] = 0
                
                if stack and stack[-1] == doll:
                    stack.pop()
                    count += 2
                else:
                    stack.append(doll)
                break
    
    return count