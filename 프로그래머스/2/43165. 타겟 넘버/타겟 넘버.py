def solution(numbers, target):
    answer = 0
    count = 0
    def dfs(sum, h):
        if h == len(numbers):
            if sum == target:
                return 1
            return 0
        s = dfs(sum + numbers[h], h+1) + dfs(sum - numbers[h], h+1)
        
        return s
    
    return dfs(0, 0)