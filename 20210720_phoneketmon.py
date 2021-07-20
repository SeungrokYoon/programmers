"""
최대값을 구하는 것인데, 중복을 없애는 것은 set을 사용하면 되고, 조합은 itertooles 에서 combinations를 사용하면 되겠다.


from itertools import combinations
def solution(nums):
    answer = 0
    combi = list(map(set, combinations(nums, int(len(nums)/2))))

    for i in combi:
        if len(i) >answer:
            answer =len(i)

    return answer
이 코드는 시간초과가 나와서 코드를 수정해야 한다. 문제를 다시 보자.
이 문제는 nums에서 set으로 중복을 먼저 없애고, len을 구하면, 그 len 값 이 n 개 폰켓몬을 선택할 떄의 최대값이 된다.
"""


def solution(nums):
    answer = 0
    a = set(nums)
    max_len = len(a)
    if max_len > int(len(nums) / 2):
        answer = int(len(nums) / 2)
        return answer
    answer = max_len
    return answer