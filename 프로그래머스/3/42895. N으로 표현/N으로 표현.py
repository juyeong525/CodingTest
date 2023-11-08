def solution(N, number):
    answer = -1
    dp = []
    for k in range(1, 9):
        set_list = set()
        set_list.add(int(str(N)*k))
        for j in range(0, k-1):
            for first in dp[j]:
                for second in dp[-j-1]:
                    set_list.add(first + second)
                    set_list.add(first * second)
                    if second != 0:
                        set_list.add(first // second)
                    set_list.add(first - second)
        if number in set_list:
            answer = k
            break
        dp.append(set_list)
    return answer