#1. 쌩으로 구현했는데 틀렸대.
import sys


def solution(scoville, K):
    answer = 0
    # 힙입력
    minHeap = MinHeap(1000000)
    for _ in scoville:
        minHeap.insert(_)

    while minHeap.Heap[minHeap.FRONT] < K:
        first = minHeap.extractMin()
        second = minHeap.extractMin()
        print("first, second ", (first, second))
        minHeap.insert(first + (second * 2))
        if minHeap.size == 2 and minHeap.Heap[minHeap.FRONT] < K:
            return -1
        answer += 1
    return answer


class MinHeap: 
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -sys.maxsize - 1
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return pos * 2

    def rightChild(self, pos):
        return pos * 2 + 1

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] >= self.Heap[self.leftChild(pos)]) or (
                    self.Heap[pos] >= self.Heap[self.rightChild(pos)]):
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.Heap[pos], self.Heap[self.leftChild(pos)] = self.Heap[self.leftChild(pos)], self.Heap[pos]
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.Heap[self.rightChild(pos)], self.Heap[pos] = self.Heap[pos], self.Heap[self.rightChild(pos)]
                    self.minHeapify(self.rightChild(pos))

    def insert(self, value):
        if self.size > self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = value
        current = self.size
        while (self.Heap[current] <=
               self.Heap[self.parent(current)]):
            self.Heap[current], self.Heap[self.parent(current)] = self.Heap[self.parent(current)], self.Heap[current]
            current = self.parent(current)
        self.PRINT()

    def isLeaf(self, pos):
        if (pos >= self.size // 2) and (pos <= self.size):
            return True
        return False

    def extractMin(self):
        popped = self.Heap[self.FRONT]
        print("popped : ", popped)

        current = self.FRONT
        self.Heap[current] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(current)
        self.PRINT()

        return popped

    def _PRINT_(self):
        for a in range(self.FRONT, self.size + 1):
            print("CURRENT: ", self.Heap[a], "\nLC: ", self.Heap[self.leftChild(a)], "\nRC: ",
                  self.Heap[self.rightChild(a)])
    def PRINT(self):
        print(self.Heap[self.FRONT: self.size + 1])

#heapq library 이용하기.->이러면 통과

import heapq
def solution2(heap, K ):
    answer=0
    heapq.heapify(heap)
    while heap[0] <K:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first+second*2)
        answer+=1
        if heap[0]<K and len(heap)==1 :
            return -1
    return answer

def solution3(alist, K ):
    heap=[]
    answer=0
    # heapq.heapify(heap)
    for a in alist:
        heapq.heappush(heap,a)
    while heap[0] <K:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first+second*2)
        answer+=1
        if heap[0]<K and len(heap)==1 :
            return -1
    return answer

print(solution3([10, 9, 6, 5, 4, 3, 2, 1],10))







