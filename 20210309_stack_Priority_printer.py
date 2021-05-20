from collections import deque


# 결국 내림차순 정리 아닐까요
def isLargerExist(docu, rest):
    for i in rest:
        if docu[0] < i[0]:
            return True
    return False

def solution(priorities, location):
    answer = 0  # 몇 번째에 인쇄되냐
    queues = deque([(value,index) for index,value in enumerate(priorities)])
    print(queues)

    while queues.__len__() !=0:
        docu = queues.popleft()

        if (isLargerExist(docu, queues)):
            queues.append(docu)
        else:
            # 여기서 출력
            answer+=1
            if docu[1] ==location:
                return answer

#다른 사람의 풀이 any 사용이 눈에 띄어서 가져와봤다.
def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print(solution([1, 1, 9, 1, 1, 1],	0))