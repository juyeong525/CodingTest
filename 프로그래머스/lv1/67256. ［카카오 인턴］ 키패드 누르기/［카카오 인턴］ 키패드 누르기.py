def solution(numbers, hand):
    keyPad = [[1,4,7],[2,5,8,0],[3,6,9]]
    currentHand = [10,12]
    answer = ''
    for number in numbers:
        if number in keyPad[0]:
            currentHand[0] = number
            answer += "L"
        elif number in keyPad[2]:
            currentHand[1] = number
            answer += "R"
        else:
            if number == 0 :
                number = 11
            left = abs(number - currentHand[0]) // 3 + abs(number - currentHand[0]) % 3
            right = abs(number - currentHand[1]) // 3 + abs(number - currentHand[1]) % 3
            print(number)
            print(left, currentHand[0])            
            print(right, currentHand[1])
            if left < right:
                currentHand[0] = number
                answer += "L"
            elif left > right:
                currentHand[1] = number
                answer += "R"
            else:
                if hand[0].upper() == "L":
                    currentHand[0] = number
                else:
                    currentHand[1] = number
                answer += hand[0].upper()
            
    return answer