import heapq


def solution(jobs):
    heapq.heapify(jobs)
    currentT= 0
    size =len(jobs)
    waitingHeap=[]
    finished= 0
    answer=0
    while finished <size:
        stop=False
        while not stop:
            if len(jobs)==0:
                break
            job = heapq.heappop(jobs)
            if job[0] <= currentT:
                heapq.heappush(waitingHeap, [job[1],job[0]])
            else:
                heapq.heappush(jobs,job)
                stop=True
        if len(waitingHeap)!=0:
            popped= heapq.heappop(waitingHeap)
            temp = popped[0]+currentT-popped[1]
            answer += temp
            currentT+= popped[0]
            finished+=1
        #멀리 떨어져 있는 잡일 경우를 처리하기 위해 시간을 하나 올려주기
        else:
            if len(jobs) !=0:
                currentT +=1

    return int(answer/size)

jobs = [ [1, 9], [2, 6],[20, 3]]
print(solution(jobs))