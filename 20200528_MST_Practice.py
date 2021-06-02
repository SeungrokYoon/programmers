"""
MST(Minimum Spanning Tree) 최소 신장트리 알고리즘 알아보기
"""

"""
Union find 부터 알고 와야 한다. cycle 이 있는지 없는지 확인해야 하기 때문

https://www.geeksforgeeks.org/union-find/

part1. Union find - naive version
"""
#code
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.v= vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def find_parent(self,parent, i):
        if parent[i] ==-1:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, x,y):
        parent[x] =y

    def isCyclic(self):
        parent = [-1] *(self.v)
        for i in self.graph:
            for j in self.graph[i]:
                x=self.find_parent(parent,i)
                y=self.find_parent(parent,j)
                if x==y:
                    return True
                self.union(parent,x,y)

graph =Graph(3)
graph.addEdge(0,1)
graph.addEdge(1,2)
graph.addEdge(1,2)
print(graph.graph)
if graph.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")


"""
part2. Union find - union by rank and path compression 
"""
class Graph_2:
    def __init__(self, n_of_vertex):
        self.n_of_vertex = n_of_vertex
        self.edges = defaultdict(list)

    def addEdge(self,u,v):
        self.edges[u].append(v)

class Subset:
    def __init__(self,parent,rank):
        self.parent = parent
        self.rank = rank
def find(subsets, n):
    if subsets[n].parent != n:
        #즉 자식 노드면:
        subsets[n].parent = find(subsets, subsets[n].parent)
    return subsets[n].parent

def union(subsets, u,v):
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
        subsets[u].rank +=1
    elif subsets[u].rank <subsets[v].rank:
        subsets[u].parent = v
        subsets[v].rank +=1
    else:
        subsets[v].parent = u
        subsets[u].rank += 1

def isCyclic(graph):
    subsets =[]
    for u in range(graph.n_of_vertex):
        subsets.append(Subset(u,0))
    for u in graph.edges:
        u_rep = find(subsets,u)
        for  v in graph.edges[u]:
            v_rep = find(subsets,v)
            if  u_rep == v_rep :
                return True
            else:
                #내가 여기서 틀림.  왜 u_rep, v_rep 를 union 해야 하는가에 대해서 다시 생각해 보기 바라.
                union(subsets, u_rep,v_rep)


g =Graph_2(5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(3,4)
g.addEdge(2,3)
g.addEdge(1,4)
if isCyclic(g):
    print("In g: Graph contains cycle")
else:
    print("In g: Graph does not contain cycle")




"""
1. Kruskal's MST Algorithm
https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

1. Prim's MST Algorithm


"""







"""
2. Prim's MST Algorithm
https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

"""