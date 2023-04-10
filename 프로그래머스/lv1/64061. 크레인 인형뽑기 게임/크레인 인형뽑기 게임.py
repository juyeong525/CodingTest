def solution(board, moves):
    stack = []
    count = 0
    for move in moves:
        for i in range(0, len(board)):
            print(move, board[i][move-1])
            if board[i][move-1] != 0 :
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                if len(stack) > 1:
                    if stack[-2] == stack[-1]:
                        stack.pop()
                        stack.pop()
                        count += 2
                break
    return count