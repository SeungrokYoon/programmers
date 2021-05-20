def solution(tickets):
    answer = []
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            temp = dfs(tickets, i)
            if temp != []:
                answer.append(temp)
    answer.sort(key=lambda u: u[1])
    print(answer)
    return answer[0]


def dfs(tickets, root):
    nodes = ["ICN"]
    visited = list()
    stack = list()
    stack.append([root, tickets[root]])

    while stack:
        ticket = stack.pop()
        visited.append(ticket)
        nodes.append(ticket[1][1])
        departure = ticket[1][0]
        new_departure = ticket[1][1]
        temp = list()
        for i in range(len(tickets)):
            if [i, tickets[i]] not in visited and tickets[i][0] == new_departure:
                temp.append([i, tickets[i]])
        if temp == []:
            break
        temp = sorted(temp, key=lambda u: u[1][1], reverse=True)
        # 여기서 정렬해주기 알파벳 앞서는게 먼저 pop될 수 있게
        stack += temp

    if len(nodes) == len(tickets) + 1:
        return nodes
    return []

if __name__ == '__main__':
    tickets =[["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "CCC"]]
    print(solution(tickets))