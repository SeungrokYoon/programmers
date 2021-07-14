def solution(lines):
    answer = 0
    l = []
    for line in lines:
        # 모든 시간을 ms로 변환하기
        day, time, work = line.split(' ')
        hh = int(time[:2]) * 3600
        mm = int(time[3:5]) * 60
        ss = int(time[6:8])
        ms = int(time[9:])
        end = (hh + mm + ss) * 1000 + ms


        work = int(float(work[:-1])*1000)

        start = end - work + 1
        end +=999
        #여기가 제일 핵심! 반드시 시작과 끝점을 따로 저장을 해야한다. 그래야 누적확인이 가능!
        l.append((time,start, 0))
        l.append((time,end, 1))
    l.sort(key = lambda x: (x[1],x[2]))

    working = 0
    max_cnt = 0
    for t in l:
        if t[2] ==0:
            working+=1
        else:
            working-=1
        max_cnt =max(working, max_cnt)
    return max_cnt