def solution(park, routes):

    # 공원의 높이와 너비 계산
    H = len(park)
    W = len(park[0])

    # 시작점 "S"의 인덱스 추출
    for i, element in enumerate(park):
        arr = list(element)
        if "S" in arr:
            start = [i, list(arr).index("S")]

    pos = start

    for route in routes:

        # 명령어 입력 처리
        op, n = route.split(' ')
        n = int(n)

        obstacle = 0  #장애물을 마주칠시 1로 바뀌는 변수(스위치)


        # 북쪽으로 이동하는 경우
        if op == 'N':
            if pos[0] - n < 0:
                print("Out of range: N")
                continue
            else:
                for i in range(1, n+1):
                    if "X" == park[pos[0] - i][pos[1]]:
                        obstacle = 1
                        print("Obstacle encountered: N")
                        continue

            if obstacle == 1:
                continue
            else:
                pos[0] -= n
                print("Operation Complete: N")

        # 남쪽으로 이동하는 경우
        elif op == 'S':
            if pos[0] + n > H-1:
                print("Out of range: S")
                continue
            else:
                for i in range(1, n+1):
                    if "X" == park[pos[0] + i][pos[1]]:
                        obstacle = 1
                        print("Obstacle encountered: S")
                        continue

            if obstacle == 1:
                continue
            else:                
                pos[0] += n
                print("Operation Complete: S")

        # 서쪽으로 이동하는 경우
        elif op == 'W':
            if pos[1] - n < 0:
                print("Out of range: W")
                continue
            else:
                for i in range(1, n+1):
                    if "X" == park[pos[0]][pos[1] - i]:
                        obstacle = 1
                        print("Obstacle encountered: W")
                        continue

            if obstacle == 1:
                continue
            else:
                pos[1] -= n
                print("Operation Complete: W")

        # 동쪽으로 이동하는 경우
        elif op == 'E':
            if pos[1] + n > W-1:
                print("Out of range: E")
                continue
            else:
                for i in range(1, n+1):
                    if "X" == park[pos[0]][pos[1] + i]:
                        obstacle = 1
                        print("Obstacle encountered: E")
                        continue
            if obstacle == 1:
                continue
            else:
                pos[1] += n
                print("Operation Complete: W")


    answer = [pos[0], pos[1]]
    return answer