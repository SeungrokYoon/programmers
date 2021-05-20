# 결국 내림차순이 몇개냐 세는 문제임
def solution(progresses, speeds):
    day = []
    for index, progress in enumerate(progresses):
        quo = (100 - progress) // speeds[index]
        if quo < (100 - progress) / speeds[index]:
            quo += 1
        day.append(quo)

    criteria = day[0]
    counter = 1
    answer = []

    for time in day[1:]:
        if time <= criteria:
            counter += 1
            continue
        else:
            answer.append(counter)
            counter = 1
            criteria = time
    answer.append(counter)

    return answer