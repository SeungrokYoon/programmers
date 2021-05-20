"""
리스트에서 가장 큰 세 개의 숫자를 return 하는 함수를 작성하라. 단, 리스트를 정렬하지는 않아야 한다.
{2, 88, 87, 16, 42, 10, 34, 1, 43, 56}

"""
import math
import time
def solution (customers):

    largest=[math.inf]
    for i in range(3):
        maxNum=largest[i]
        starting = 0
        for pie in customers:
            if (pie < maxNum) and (starting <= pie):
                starting = pie
        largest.append(starting)
    return largest[1:]


def solution2 (customers):
    customers2=customers
    withFolks = []
    for i in range(3):
        maxNum = 0
        maxIndex = 0
        for n in range(len(customers2)):
            if customers2[n] >=maxNum:
                maxNum = customers2[n]
                maxIndex = n
        withFolks.append(maxNum)
        customers2 = customers2[:maxIndex] + customers2[maxIndex + 1:]
    return withFolks
#위 알고리즘은 n**2시간으로 품.
#반면에 아래 알고리즘은 n 시간으로 풀었기 때문에 굉장히 효율적임.
#with a little change of perspective and some refactoring, we've made this simple bit of code faster and more efficient.
def solution3 (customers):
    first = 0
    second =0
    third= 0
    for i in range(len(customers)):
        if customers[i] > first:
            third = second
            second = first
            first= customers[i]
        elif customers[i] > second:
            third = second
            second = customers[i]
        elif customers[i] > third:
            third = customers[i]
        else:
            continue
    return first, second, third
alist = [2, 88, 87, 16, 42, 10, 34, 1, 43, 56]
start=time.perf_counter_ns()
print(solution(alist), time.perf_counter_ns()-start)
start2=time.perf_counter_ns()
print(solution2(alist), time.perf_counter_ns()-start2)
start3 = time.perf_counter_ns()
print(solution3(alist), time.perf_counter_ns()-start3)
