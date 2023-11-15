import numpy as np
inf= float('inf')

class GRAPH:
    def __init__(self,n,C):
        self.n=n
        self.C=C
def PutGraph(G):
    print("\nNumber of nodes in the graph:",G.n)
    print("\nCost Matrix:\n")
    print(G.C)

c=[[0,8,inf,1],[inf,0,1,inf],[4,inf,0,inf],[inf,2,9,0]]
G=GRAPH(4,c)
PutGraph(G)
a=np.zeros((G.n,G.n))

for i in range(G.n):
    for j in range(G.n):
        a[i][j]=G.C[i][j]
for k in range(G.n):
    for i in range(G.n):
        for j in range(G.n):
            a[i][j]=min(a[i][j],a[i][k]+a[k][j])
print("All pairs Shortest path is given by\n",a)

        