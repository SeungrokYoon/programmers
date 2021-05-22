from collections import deque
from collections import defaultdict

"""
visited 를 단순한 방문 체크 리스트가 아니라, 시작점으로부터의 거리도 기록할 수 있다는 점이 Point!!!
"""


def solution(n, vertex):
    answer = 0
    graph = defaultdict(list)

    # graph 작성
    for i in vertex:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    visited = [0] * (n + 1)
    queue = deque([1])
    visited[1] = 1

    #bfs
    while queue:
        next_node = queue.popleft()
        for i in graph[next_node]:
            if visited[i]== 0:
                visited[i] = visited[next_node]+1
                queue.append(i)

    m = max(visited)
    answer = visited.count(m)
    return answer

n=6
vertex= [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))