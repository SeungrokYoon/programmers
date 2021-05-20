from collections import deque
from collections import defaultdict

def solution(tickets): #bfs 를 이용한 해
    answer = []
    graph = defaultdict(list)
    for ticket in range(tickets):
        graph[ticket[0]] = ticket[1]
    for t in graph:
        graph[t] = sorted(graph[t])
    answer = bfs(graph)
    return answer


def bfs(tickets, root):
    queue= deque("ICN")
    routes= []

    while queue:



    return routes


"""
더 나은 solution 
"""
def solution2(tickets):
    trip_advisor = defaultdict(list)

    for t in tickets:
        trip_advisor[t[0]].append(t[1])
    for t in trip_advisor:
        trip_advisor[t] = sorted(trip_advisor[t])

    departure = 'ICN'
    stack = [departure]
    routes = []

    while stack:
        plane = stack[-1]
        if trip_advisor[plane]:
            stack.append(trip_advisor[plane].pop(0))
        else:
            routes.append(stack.pop())
    return routes[::-1]


if __name__ == '__main__':
    tickets = [["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "CCC"],["CCC","BBB"]]
    # print(solution(tickets))
    print(solution2(tickets))