#그냥 리스트로만 푼 어딘가 불편한 코드.......이게 진짜 맞는건가.
def solution(operations):
    answer = []
    doubleHeap = []
    for oper in operations:
        print(doubleHeap)
        oper1, oper2 = oper.split()
        if oper1 == "I":
            doubleHeap.append(oper2)
            doubleHeap.sort()

        else:
            if len(doubleHeap) == 0:
                continue
            if oper2 == 1:
                doubleHeap = sorted(doubleHeap)[:-1]

            else:
                doubleHeap = sorted(doubleHeap)[1:]
    if len(doubleHeap) == 0:
        answer = [0, 0]
    else:
        answer = [doubleHeap[-1], doubleHeap[0]]
    return answer


#double linked list 를 통한 구현
class Node:
    def __init__(self,val):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None

class DoubleEndPriorityQueue:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):

    def findMax(self):

    def findMin(self):
        return self.root

    def delete(self,val):

    def

import heapq
def solution2(opreations):
    answer=[]
    minHeap = []
    maxHeap = []
    for command in opreations:
        print(max)
        operation, operand = command.split()
        operand =  int(operand)
        if operation =="I":
            heapq.heappush(minHeap, operand)
            heapq.heappush(maxHeap, -operand)

        else:
            if minHeap ==[] and maxHeap ==[]:
                return [0,0]
            if operand ==1:
                heapq.heappop(maxHeap)

            else:
                heapq.heappop(minHeap)
    return answer
operations= ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution2(operations))