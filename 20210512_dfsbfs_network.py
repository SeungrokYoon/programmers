"""
네트워크 찾기
dfs 알고리즘으로 시작했지만, 2개 빼고 다 오답.
이유를 찾아봤더니, 이러한 상하좌우에 대한 접근은 각 노드의 좌표로 해석할 때이고,
이 문제는 인접행렬 개념으로 접근해야 한다고 함.
"""

def solution(n, computers):
    answer = 0
    visited = [False]*n

    def dfs(computers, start):
        x, y = start
        if computers[x][y] == 0:
            return False
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        if computers[x][y] == 1:
            computers[x][y] = 0  # 0으로 방문처리 해놓고, dfs
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                dfs(computers, (nx, ny))
            return True

    for i in range(n):
        for j in range(n):
            if dfs(computers, (i, j)) == True:
                answer += 1


    return answer


"""다른 사람의 풀이"""

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            print(j)
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer
print(solution(3,[[1,0,1],[0,1,0],[1,0,1]]))

"""union find를 이용한 해법"""

class DisjointSet:
    def __init__(self,n):
        self.data = list(range(n))
        self.size =n
    def find(self,index):
        return self.data[index]


    def union(self,x,y):
        x,y = self.find(x), self.find(y)

        if x ==y:
            return
        for i in range(self.size):
            if self.find(i) ==y:
                self.data[i]=x
    @property
    def length(self):
        return len(set(self.data))


def solution(n, computers):
    answer=0
    disjoint = DisjointSet(n)
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] ==1:
                disjoint.union(i,j)
    answer = disjoint.length



    return answer

