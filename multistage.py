import numpy as np
SIZE=50
inf= float('inf')

class GRAPH:
    def __init__(self,n,C,k):
        self.n=n
        self.C=C
        self.k=k
        


def GetGraph():
    Cost=0.0
    
    n=int(input("Enter number of nodes in the graph(n):"))
    if(n<=0 or n>SIZE):
        print("\nSize Error")
        exit(0)
    k=int(input("Enter number of stages in the graph(k):"))
    C=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i!=j:
                C[i][j]=inf
            
    while(True):
        Choice=input("\nAny more edge to add(y/n)?")
        if(Choice == 'n' or Choice == 'N'):
            G=GRAPH(n,C,k)
            return G
        i,j,Cost=[int(x) for x in(input("\nEnter vertices of the edge and related cost(u,v,c):").split())]
        if(i<0 or i>=n or j<0 or j>=n or Cost <=0):
            print("\nWrong data, re-enter data")
        else:			
                #For un-directed graph
                C[i][j]=Cost


def PutGraph(G):
    print("\nNumber of nodes in the graph:",G.n)
    print("\nNumber of stages in the graph:",G.k)
    print("\nCost Matrix:\n")
    print(G.C)


G = GetGraph()
PutGraph(G)
S=int(input("\nEnter Start Vertex:"))

p=[0]*G.k
d=[0]*G.n
print(d)
cost=[inf]*G.n
cost[G.n-1]=0.0
for j in range(G.n-1,-1,-1):
    for r in range(G.n):
        if G.C[j,r]!=inf and r!=j and cost[r]+G.C[j,r]<cost[j]:
            cost[j]=cost[r]+G.C[j,r]
            d[j]=r
print(d)
p[0]=0
p[G.k-1]=G.n-1
for j in range(1,G.k-1):
    p[j]=d[p[j-1]]
print("Path array:",p)
print("Minimum cost:",cost[0])


