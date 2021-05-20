def solution(array, commands):
    answer = []
    for command in commands:
        temp =sorted(array[command[0]-1:command[1]])
        answer.append(temp[command[2]-1])
    return answer


def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))