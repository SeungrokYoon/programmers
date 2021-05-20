#https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
#코딩테스트 연습 주식가격
"""
prices	         return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

"""
prices = [1,2,3,2,3]

#0(n)복잡도로 끝내 보도록 해 보기. 스택을 사용 해보기.
#이거는 지금 n**2복잡도인데 어떡하징. -> 틀림
#다른 사람 풀이 테스트 맞고 효율성 높음
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    st = [0]
    for i in range(1,len(prices)): # 스택에 쌓은 건 아직 언제 떨어질지 모르는 시간들
        while st and prices[st[-1]] > prices[i]: #스택에 뭐가 있고, 또 스택 맨 위에 것이 prices[i]보다 큰 경우
            prev = st[-1] #이전 것(prev)로 기록, 만약에 이 while문에 진입하게 되면, 이미 이건 떨어진 주가의 인덱스
            answer[prev] = i-prev #st[-1]이 맨 처음은0으로 시작했고, answer의 0번 인덱스에 1-0으로 들어갔음
            st.pop() #하나 빼버림
        st.append(i) #st 가 비어있어서 더 pop하지 못하는 상황 , 또는 prices의 맨 위에 인덱스 가격(prices[i-1])과 prices[i] 비교

    for sec in st:
        answer[sec] = i - sec
    return answer

#0(n)복잡도로 끝낼 수 있는 문젠가?
#아니 이걸 어떻게 quadratic 으로 하지 않고 풀 수 있냐
#테스트는 맞는데, 효율성 초과
def solution(prices):
    length = len(prices)
    answer = [0]*length
    counter = 1
    while counter < length:
        prev= prices[counter-1]
        tempQueue = prices[counter:]
        for e in tempQueue:
            if prev <= e:
                answer[counter-1] += 1
            else:
                answer[counter-1] += 1
                break
        counter+=1
    return answer

"""
[1, 2, 3, 2, 3]

"""

