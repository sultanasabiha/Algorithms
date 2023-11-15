
import numpy as np
SIZE=50
inf= float('inf')

class GRAPH:
    def __init__(self,n,C):
        self.n=n
        self.C=C


def PutGraph(G):
    print("\nNumber of nodes in the graph:",G.n)
    print("\nCost Matrix:\n")
    print(G.C)

c=[[0,4,4,inf,inf,inf],[4,0,2,inf,inf,inf],[4,2,0,3,2,4],[inf,inf,3,0,inf,3],[inf,inf,2,inf,0,3],[inf,inf,4,3,3,0]]
G=GRAPH(6,c)
PutGraph(G)
S=0
selected = [False]*G.n

no_edge = 0
mincost=0.0

selected[S] = True
print("\n  Edge  :  Weight")
while (no_edge < G.n - 1):
    minimum = inf
    x = 0
    y = 0
    
    for i in range(G.n):
        if selected[i]:
            for j in range(G.n):
                if ((not selected[j]) and (G.C[i][j]!=0 or G.C[i][j]!=inf)):  
                    # not in selected and there is an edge
                    if minimum > G.C[i][j]:
                        minimum = G.C[i][j]
                        x = i
                        y = j
    print(str(x) + "  -  " + str(y) + "  :  " + str(G.C[x][y]))
    mincost+=G.C[x][y]
    selected[y] = True
    no_edge += 1

print("Minimum Cost:",mincost)



