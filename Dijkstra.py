
import numpy as np
SIZE=50
inf= float('inf')

class GRAPH:
    def __init__(self,n,C):
        self.n=n
        self.C=C
        


def GetGraph():
    Cost=0.0
    
    n=int(input("Enter number of nodes in the graph(n):"))
    if(n<=0 or n>SIZE):
        print("\nSize Error")
        exit(0)

    C=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i!=j:
                C[i][j]=inf
            
    while(True):
        Choice=input("\nAny more edge to add(y/n)?")
        if(Choice == 'n' or Choice == 'N'):
            G=GRAPH(n,C)
            return G
        i,j,Cost=[int(x) for x in(input("\nEnter vertices of the edge and related cost(u,v,c):").split())]
        if(i<0 or i>=n or j<0 or j>=n or Cost <=0):
            print("\nWrong data, re-enter data")
        else:			
                #For un-directed graph
                C[i][j]=Cost


def PutGraph(G):
    print("\nNumber of nodes in the graph:",G.n)
    print("\nCost Matrix:\n")
    print(G.C)
   
def to_be_visited():
    
    j =-10
    for i in range(G.n):
        if v[i] == False and (j < 0 or dist[i] <= dist[j]):
            j = i
    return j

G = GetGraph()
PutGraph(G)
S=int(input("\nEnter Start Vertex:"))

global v
v=[False]*G.n
global dist
dist=[G.C[0][i] for i in range(G.n)]

v[0]=True
dist[0]=0.0

for j in range(2,G.n):

    # Find next vertex to be visited
    u= to_be_visited()
    for w in range(G.n):

        # Updating new distances
        if G.C[u][w] != inf and G.C[u][w] != 0 and v[w] == False:
            new_distance = dist[u]+ G.C[u][w]
            if dist[w] > new_distance:
                dist[w] = new_distance
        
        v[u]=1

print(dist)
# Printing the distance
for i in range(G.n):
    print("Distance of ",i," from ",S,": ", dist[i])
