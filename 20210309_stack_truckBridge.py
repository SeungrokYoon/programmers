from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridgeQ=deque([0]*bridge_length)
    position = -1
    answer=0
    tempSum=0
    numTruck= len(truck_weights)
    while position < numTruck-1:
        nextNum= truck_weights[position+1]
        tempSum -= bridgeQ.popleft()
        if tempSum + nextNum <= weight:
            bridgeQ.append(nextNum)
            position+=1
            tempSum += nextNum
        else:
            bridgeQ.append(0)
        answer+=1
    answer+= bridge_length
    return answer
print(solution(2,10,[7,4,5,6]))
"""
이 문제의 핵심은 스택에 쌓아놓고 검증을 윈도우를 하는 것. 트럭이 다 지나갈 때까지 큐의 길이 *1초 만큼 기다려야 하니까 결국
큐의 길이가 결국에는 답이 된다.

*5번 예제가 시간초과가 뜨는데, 이는 sum메소드 때문에 그런 것으로 sum을 사용하지 않고 sum을 최신화 하는 방향으로 유지해보자.  
그리고 deque(double-end-que)


"""