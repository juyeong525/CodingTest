def solution(people, limit):
    answer = 0
    people.sort() # 정렬 후 몸무게 큰 사람과 작은사람 짝지어야 많이 태울 수 있을 것 같음
    start = 0
    end = len(people) -1
    
    while(start<=end):  # 두 명씩 구출해서 다 구출할 때까지 비교
        if(people[start]+people[end] <=limit):  # limit 보다 작거나 같으면 둘다 구출 가능
            start +=1
            end -=1
        else:  # 안되면 일단 몸무게 큰 사람부터 먼저 구출
            end-=1
        answer +=1
    return answer