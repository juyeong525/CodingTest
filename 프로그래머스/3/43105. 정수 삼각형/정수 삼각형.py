from collections import defaultdict


def solution(triangle):
    memo = defaultdict(int)
    memo[(0,0)] = triangle[0][0]

    for x in range(1, len(triangle)):
        for y in range(len(triangle[x])):
            memo[(x,y)] = triangle[x][y] + max(memo[(x-1,y-1)], memo[(x-1,y)])

    return max(memo.values())