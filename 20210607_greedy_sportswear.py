"""
문제링크 : https://programmers.co.kr/learn/courses/30/lessons/42862

탐욕법 - 체육복

"""
def solution(n, lost, reserve):
    borrowed = [0] + [1] * n
    answer = 0
    for i in lost:
        borrowed[i] -= 1
    for i in reserve:
        borrowed[i] += 1

    for i in range(1, n + 1):
        if borrowed[i] == 2:
            if i - 1 >= 1 and i + 1 > n:
                if borrowed[i - 1] == 0:
                    borrowed[i - 1] = 1
                    borrowed[i] -= 1
            elif i - 1 < 1 and i + 1 <= n:
                if borrowed[i + 1] == 0:
                    borrowed[i + 1] = 1
                    borrowed[i] -= 1
            else:
                if borrowed[i - 1] == 0 and borrowed[i + 1] != 0:
                    borrowed[i - 1] += 1
                    borrowed[i] -= 1
                elif borrowed[i - 1] != 0 and borrowed[i + 1] == 0:
                    borrowed[i + 1] += 1
                    borrowed[i] -= 1
                else:
                    borrowed[i - 1] += 1
                    borrowed[i] -= 1

    for i in borrowed:
        if i != 0:
            answer += 1

    return answer