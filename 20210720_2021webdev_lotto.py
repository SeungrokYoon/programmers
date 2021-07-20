"""
raw 하게 비교했을 때가 최저순위.
여기에 +0의 개수만큼 추가를 하면 최대 등수가 되려나
함정은 6등은 1개 번호, 0개 번호가 일치할 떄라는거!

else 예약어를 최대한 자제하면서 코딩했다.
"""

def solution(lottos, win_nums):
    answer = [0,7]
    for i in lottos:
        if i==0:
            answer[0] += 1
        if (i != 0) and (i in win_nums):
            answer[1] -= 1
    #예외처리해주기
    if answer[1] ==7:
        if answer [0] ==0:
            answer[0] = 6
            answer[1] = 6
            return answer
        answer[0] = answer[1] - answer[0]
        answer[1] = 6
        return answer
    answer[0] = answer[1] - answer[0]
    return answer