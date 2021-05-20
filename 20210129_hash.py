def solution(participant, completion):
    answer = ''
    tempDict = {}
    # make dictionary
    # 동명이인 처리를 해야함.
    tempSet= list(set(participant))
    tempDict = {k:[] for k in tempSet}

    #해당 키가 존재하는 인덱스를 딕셔너에 추가한다. 이러면 중복된 녀석들을 하나로 모을 수 있
    for index, element in enumerate(participant):
        tempDict[element].append(index)
    # search using hash functions
    for matter in completion:
        if len(tempDict[matter])==1:
            del tempDict[matter]
        else:
            tempDict[matter]= tempDict[matter][:-1]
    answer =list(tempDict.keys())[0]
    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))