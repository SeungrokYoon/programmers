
"""
link = https://programmers.co.kr/learn/courses/30/lessons/42746#

문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

"""

#string 을 sort 하면, int 크기가 아니라 사전순 정렬임. 한 번 시험해보자 .
#sort 함수는 시간 복잡도가 nlogn 이니까 간단
templist= [3, 30, 34, 5, 9]
templist2= [1,121,3,30,34,39,329,398,399,5,999]
templist3 = [30,3,34,39,300,329 ]
"""
키 포인트는 예제에서 볼 수 있다시피 303 보다 330 이 더 크다는 것이었다. 따라서 나는 최소값부터 
차례차례 더해나가는 방식을 선택했다.

"""
def solution(numbers):
    dic={}
    for a in range(1,10):
        dic[str(a)] = []
    answer = ''
    for num in numbers:
        dic[str(num)[0]].append(str(num))
    for starting in range(1,10):
        tempSum=''
        sortedList = sorted(dic[str(starting)])
        for x in sortedList:
            option1 = tempSum + x
            option2 = x+ tempSum
            if option1 >=option2 :
                tempSum = option1
            else:
                tempSum = option2
        answer = tempSum + answer
    return answer
# print(solution(templist))
# print(solution(templist2))
# print(solution(templist3))

"""
위 방식은 얼핏 보면 문제를 해결한 것 같지만 전혀 그렇지 않음. 

읽기목록 : https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
여러 정렬 알고리즘이 존재하는데, 이들은 여러 특징들을 가지고 있다. 
나는 어떤 때에 어떤 정렬 알고리즘을 사용해야 하는지 아직 잘 모르는 것 같다. 
 
핵심 개념은 : comparison - based sorting 이란 것인데, 흔히 우리가 요소들끼리의 비교를 통해서 정렬하는 알고리즘들이 여기에 포함됨. 
나도 비슷하게 접근했지만, 핵심은 ab ba 비교를 통한 정렬에 있음. 나는 ab ba 비교를 해서 바로 answer에 넣었지만, 그게 아니고, 
정렬을 다 하고 나서 한꺼번에 합치는 것이 뽀인트였다!
"""
#버블정렬을 통한 해법
def solution2(number):

    numbers = number
    print("original : ", numbers)
    answer = ''
    for size in range(len(numbers),0,-1):
        for index in range(size-1):
            option1 = int(str(numbers[index]) + str(numbers[index+1]))
            option2 = int(str(numbers[index+1]) + str(numbers[index]))
            print(option1, option2)
            if option1 > option2 :
                print("change")
                numbers[index],numbers[index+1] = numbers[index+1] , numbers[index]
    for _ in numbers:
        answer = str(_) + answer
    return answer

"""
MergeSort를 직접 구현하여 변형한 뒤, 이를 정렬 알고리즘으로 사용하였음.
#MergeSort 를 통한 해법 - > nlogn 시간으로 시간초과에는 걸리지 않았으나, 
테스트 11을 풀지 못하고 정확도 90%에서 막혔음.
"""

def MergeSort(target):
    if len(target) > 1:
        mid = len(target) // 2
        L = target[:mid]
        R = target[mid:]
        MergeSort(L)
        MergeSort(R)
        i = j=k=0
        #여기서 변형이 들어간다.
        while i < len(L) and j < len(R):
            print(int(str(L[i])+str(R[j])),int(str(R[j])+str(L[i])))
            if int(str(L[i])+str(R[j])) > int(str(R[j])+str(L[i])) :
                target[k] = R[j]
                j+=1
            else:
                target[k] = L[i]
                i+=1
            k+=1
        while i<len(L):
            target[k] = L[i]
            i+=1
            k+=1
        while j<len(R):
            target[k] = R[j]
            j+=1
            k+=1
def solution3(number):
    numbers = number
    print("original : ", numbers)
    answer = ''
    MergeSort(numbers)
    print("After MergeSort: ",numbers)
    for _ in numbers:
        answer = str(_) + answer
    return str(int(answer))

print(solution3([0,9,2,1,10,19]))

"""다른 사람의 풀이 더 깔끔하고, Pythonic 하다. """


import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution4(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer