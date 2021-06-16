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



class Graph:
    def __init__(self,n_of_vertices):
        self.n_of_vertices = n_of_vertices
        self.edges = defaultdict(list)
    def addEdges(self, u ,v):
        self.edges[u].append(v)


class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

def find(subsets, node):
    if subsets[node].parent !=node:
        find(subsets, subsets[node].parent)
    return subsets[node].parent


def union(subsets, u_rep, v_rep):
    if subsets[u_rep].rank > subsets[v_rep].rank:
        subsets[v_rep].parent = u_rep
        subsets[u_rep].rank += 1

    elif subsets[u_rep].rank < subsets[v_rep].rank:
        subsets[u_rep].parent = v_rep
        susbsets[v_rep].rank +=1
    else:
        subsets[v_rep].parent = u_rep
        subsets[u_rep].rank +=1


def isCyclic(graph):
    subsets = []
    # subsets 초기화
    for i in range(graph.n_of_vertices):
        subsets.append(Subset(i, 0))

    for u in graph.edges:
        u_rep = find(subsets, u)
        for v in graph.edges[u]:
            v_rep = find(subsets, v)
            if u_rep != v_rep:
                union(subsets, u_rep, v_rep)
            else:
                print("There is cycle in the graph")



"""
1. Kruskal's MST Algorithm
https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
"""



"""
2. Prim's MST Algorithm
https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
구현 연습
https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1

궁금증: 그렇다면 Prim's Algorithm 에서는 사이클 판별을 어떻게 하는 것일까? 자동으로 사이클이 판별이 되나?
궁금증2: 시간 복잡도는 adj matrix - O(V^^2), adj list - O(E*LogV)
"""
#Prim's algorithm with adj matrix

#Prim's algorithm with adj list + full implementation of heap
from collections import defaultdict
import sys
class Heap:
    def __init__(self):
        self.array=[]
        self.size=[]
        self.pos=[]

    def newMinHeapNode(self,v,dist):
        minHeapNode = [v,dist]
        return minHeapNode

    def swapMinHeapNode(self,a,b):
        t=self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def minHeapify(self,idx):
        smallest= idx
        left= 2*idx +1
        right = 2*idx +2
        if left <self.size and self.array[left][1] < self.array[smallest][1]:
            smallest =left
        if right <self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        if smallest !=idx:
            self.pos[self.array[smallest][0]] =idx
            self.pos[self.array[idx][0]] = smallest

            self.swapMinHeapNode(smallest, idx)
            self.minHEapify(smallest)

    def extractMin(self):
        if self.isEmpty() ==True:
            return
        root= self.array[0]
        lastNode= self.array[self.size -1]
        self.array[0] = lastNode
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size-1

        self.size -=1
        self.minHeapify(0)
        return root

    def isEmpty(self):
        return True if self.size ==0 else False

    def decreaseKey(self,v,dist):
        i=self.pos[v]
        self.array[i][1] = dist
        while i>0 and self.array[i][1] < self.array[(i-1)/2][1]:
            self.pos[self.array[i][0]] = (i-1)/2
            self.pos[self.array[(i-2)/2][0]] = i
            self.swapMinHeapNode(i, (i-1)/2)
            i= (i-1)/2

    def isInMinHeap(self,v):
        if self.pos[v] <self.size:
            return True
        return False

def printArr(parent, n):
    for i in range(1,n):
        print("%d -%d" %(parent[i],i))

class Graph:
    def __init__(self,V):
        self.V=V
        self.graph = defaultdict(list)





