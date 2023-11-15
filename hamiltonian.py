
SIZE=50
inf=float('inf')

class GRAPH:
    def __init__(self,n,C):
        self.n=n
        self.C=C

def PutGraph(G):
    print("\nNumber of nodes in the graph:",G.n)
    print("\nAdjacency Matrix:\n")
    print(G.C)

def hamil(k):
    while(True):
        next(k)
        if(x[k]==0):
            return
        if k==G.n-1:
            print(x)
        else:
            hamil(k+1)
def next(k):
    while True:
        x[k]=(x[k]+1)%(G.n)
        #print(x)
        if x[k]==0:
            return
        if G.C[x[k-1]][x[k]]!=0:
            #print(G.C[x[k-1]][x[k]]!=0)
            j=0
            for j in range(k):
                if x[k]==x[j]:
                    break
            #print(j==k)
            if (j+1)==k:
                if ((k<G.n-1) or ((k==G.n-1) and G.C[x[G.n-1]][x[0]]!=0)):
                    return
#G = GetGraph()


c=[[0,1,0,1,0],[1,0,1,1,1],[0,1,0,1,1],[1,1,1,0,0],[0,1,1,0,0]]
G=GRAPH(5,c)
PutGraph(G)
global x
x=[0]*G.n
x[0]=0
global k
k=1
print("The Hamiltonian cycles present are:" )
hamil(k)
