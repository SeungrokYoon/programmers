from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    max_level = len(numbers)-1
    current_index = 0
    queue.append([numbers[0], current_index])
    queue.append([-numbers[0], current_index])
    while queue:
        thisNum = queue.popleft()
        if thisNum[1] == max_level and thisNum[0] == target:
            answer += 1
        else:
            if thisNum[1] < max_level:
                queue.append([thisNum[0] + numbers[thisNum[1]+1 ],thisNum[1]+1 ])
                queue.append([thisNum[0] - numbers[thisNum[1]+1],thisNum[1]+1 ])

    return answer
numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))
