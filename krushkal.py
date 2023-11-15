# Kruskal's algorithm in Python


SIZE=50
inf=100

class GRAPH:
    def __init__(self,n,edgelist):
        self.n=n
        self.edgelist=edgelist


def GetGraph():
    edge=[]
    
    n=int(input("Enter number of nodes in the graph(n):"))
    if(n<=0 or n>SIZE):
        print("\nSize Error")
        exit(0)
            
    while(True):
        Choice=input("\nAny more edge to add(y/n)?")
        if(Choice == 'n' or Choice == 'N'):
            print("No. og vertices:",n)
            print("Edgelist:\n",edge)
            G=GRAPH(n,edge)
            return G
        edge.append(list(int(x) for x in(input("\nEnter vertices of the edge and related cost(u,v,c):").split())))
        

'''def PutGraph(G):
    print("\nNumber of nodes in the graph:",G.n)
    print("\nCost Matrix:\n")
    print(G.C)
'''  
def Find(parent, i):
        if parent[i] == i:
            return i
        return Find(parent, parent[i])
def union( parent, rank, x, y):
        xroot = Find(parent, x)
        yroot = Find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
G = GetGraph()
#PutGraph(G)
S=int(input("\nEnter Start Vertex:"))
heap=sorted(G.edgelist,key=lambda x:x[2])

parent=[i for i in range(G.n)] #root of subtree
rank=[0]*G.n #subree size
t=[]
mincost=0.0
i=0
while((i<G.n-1) and len(heap)>0):
    e=heap.pop(0)

    u=e[0]
    v=e[1]
    j=Find(parent,u)
    k=Find(parent,v)

    if(j!=k):
        i+=1
        t.append(e)
        mincost+=e[2]
        union(parent,rank,j,k)

print("Edgelist of the minimum spanning tree:\\n",t)
print("Minimum cost:",mincost)
