"""
내가 막히는 부분:
수포자 세명에대한 조사는 다 할 수 있는데,
그러면 이 사람들을 나열하는 건 어떻게 해야 하는가
"""

def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            score[0] +=1
        if answers[i] == second[i%8]:
            score[1] +=1
        if answers[i] == third[i%len(third)]:
            score[2] +=1
    largest = max(score)
    for i, v in enumerate(score):
        if v == largest:
            answer.append(i+1)

    return answer