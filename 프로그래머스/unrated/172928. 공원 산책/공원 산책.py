def solution(park, routes):
    n, m = len(park), len(park[0])
    op = {'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0)}

    for l in park:
        print(*l)

    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        oper, count = route.split()

        flag = True
        sx, sy = x, y

        for i in range(int(count)):
            dx, dy = op[oper]
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and park[nx][ny] != 'X':
                x, y = nx, ny
            else:
                x, y = sx, sy
                break

    return x, y