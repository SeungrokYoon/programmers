"""
Time Complexity: O(ElogE) or O(ElogV).
Sorting of edges takes O(ELogE) time.
After sorting, we iterate through all edges and apply the find-union algorithm.
The find and union operations can take at most O(LogV) time.
 So overall complexity is O(ELogE + ELogV) time.
  The value of E can be at most O(V2), so O(LogV) is O(LogE) the same.
Therefore, the overall time complexity is O(ElogE) or O(ElogV)
"""

class Graph:
    def __init__(self, n_of_vertices):
        self.n_of_vertices= n_of_vertices
        self.graph = [] #여기서는 defaultdict(list) 가 아니라 그냥 list를 썼다. 왜냐하면 정렬을 해야하기 때문에

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self, parent, node): #find the root
        if parent[node] != node:
            parent[node]= self.find(parent, parent[node])
        return parent[node]

    def union(self,parent,rank, xroot, yroot):
        if rank[xroot] <rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] +=1

    def KruskalMST(self):
        result = []
        i=0 #index for sorted edges
        e=0 #index for result[]

        self.graph = sorted(self.graph, key = lambda item: item[2])
        print(self.graph)
        parent =[] #root를 추적
        rank=[] #rank 를 기록
        #Create V subsets with single elements
        for node in range(self.n_of_vertices):
            parent.append(node)
            rank.append(0)

        while e <self.n_of_vertices -1:
            u,v,w = self.graph[i]
            i=i+1 #가장 작은 weight를 골랐으니 그 다음으로 포인터를 옮겨주기
            x=self.find(parent,u)
            y=self.find(parent,v)

            if x!=y:
                e=e+1
                result.append([u,v,w])
                self.union(parent, rank, x,y)
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost +=weight
            print("%d -- %d ==%d" %(u,v,weight))
        print("Minimum Spanning Tree", minimumCost)

# Driver code
g = Graph(9)
g.addEdge(3,5,14)
g.addEdge(1,7,11)
g.addEdge(5,4,10)
g.addEdge(3,4,9)
g.addEdge(1,2,8)
g.addEdge(0,7,8)
g.addEdge(7,8,7)
g.addEdge(2,3,7)
g.addEdge(8,6,6)
g.addEdge(2,5,4)
g.addEdge(0,1,4)
g.addEdge(6,5,2)
g.addEdge(8,2,2)
g.addEdge(7,6,1)


# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)

# Function call
g.KruskalMST()


class Graph2:
    def __init__(self,n):
        self.n = n
        self.graph = []


    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def union(self,parents,ranks,u,v):
        if ranks[u]> ranks[v]:
            parents[v] = u
        elif ranks[u]<ranks[v]:
            parents[u] = v
        else:
            parents[v]=u
            ranks[u] +=1


    def find(self,parents,node):
        if parents[node]!=node:
            parents[node] = self.find(parents, parents[node])
        return parents[node]

    def KruskalMST(self):
        #weight에 따라 edges 를 정렬하기
        self.graph = sorted(self.graph, key = lambda x: x[2])
        parents= [0]*self.n #부모
        ranks= [0]*self.n #ranks
        answer= []
        totalWeight = 0
        for i in range(self.n):
            parents[i]=i

        pointer = 0 #smallest pointer
        counter= 0 #edge counter
        while counter < self.n-1:
            u,v,w= self.graph[pointer] #현재 smallest
            u_root = self.find(parents,u)
            v_root = self.find(parents,v)
            pointer += 1

            if u_root  != v_root :
                answer.append([u,v,w])
                print(u , " -- ",v, " == ", w)
                self.union(parents, ranks,u_root, v_root)
                totalWeight+=w
                counter+=1
        print("graph 2's MST =", totalWeight)


g2 = Graph2(9)
g2.addEdge(3,5,14)
g2.addEdge(1,7,11)
g2.addEdge(5,4,10)
g2.addEdge(3,4,9)
g2.addEdge(1,2,8)
g2.addEdge(0,7,8)
g2.addEdge(7,8,7)
g2.addEdge(2,3,7)
g2.addEdge(8,6,6)
g2.addEdge(2,5,4)
g2.addEdge(0,1,4)
g2.addEdge(6,5,2)
g2.addEdge(8,2,2)
g2.addEdge(7,6,1)
g2.KruskalMST()

