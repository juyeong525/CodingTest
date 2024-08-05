import sys 
sys.setrecursionlimit(10000)

s = 0
def solution(maps):
    isCheck = [[0] * len(m) for m in maps]
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    maxY = len(maps)
    maxX = len(maps[0])
    answer = []
    def dfs(x, y, m):
        global s
        isCheck[y][x] = 1
        if m == "X":
            return
        s += int(m)
        for dir in direction:
            xd, yd = x + dir[0] , y + dir[1]
            if 0 <= xd < maxX and 0 <= yd < maxY and isCheck[yd][xd] != 1:
                dfs(xd, yd, maps[yd][xd])
        return 
        
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            global s
            s = 0
            if maps[i][j] != "X" and isCheck[i][j] != 1:
                dfs(j, i, maps[i][j])
                answer.append(s)
    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
        return answer