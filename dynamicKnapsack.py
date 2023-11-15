import numpy as np

class Item:
    def __init__(self,p,w):
        self.p=p
        self.w=w

def knapsack(n,m):
    t=np.zeros((n+1,m+1))
    for i in range(n+1):
        for j in range(m+1):
            if i>0 and j<arr[i-1].w:
                t[i][j]=t[i-1][j]
            if i>0 and j>=arr[i-1].w:
                t[i][j]=max((arr[i-1].p+t[i-1][j-arr[i-1].w]),t[i-1][j])
    print(t)
    profit=t[n][m]

    v=np.zeros(n)
    i=n
    j=m
   
    while(i>=0 and j>=0): 
        print(i,j)  
        if t[i][j]==t[i-1][j]:
            i=i-1
        else:
            if t[i][j]==t[i-1][j-arr[i-1].w]+arr[i-1].p:
                v[i-1]=1
                j=j-arr[i-1].w
                i=i-1

    print(v)
    print("\nObjects included:")
    print("Object\tProfit\tWeight")
    for i in range(n):
        if v[i]==1:
            print(i+1,"\t",arr[i].p,"\t",arr[i].w)
    print("Maximum attainable profit:",profit)


global arr
arr=[Item(11,20),Item(21,25),Item(31,30),Item(33,40),Item(43,50),Item(53,10),Item(55,70),Item(65,10)]
#arr=[Item(3,2),Item(4,3),Item(5,4),Item(6,5)]
#arr=[Item(1,1),Item(6,2),Item(18,5),Item(22,6),Item(28,7)]
n=len(arr)
m=110
knapsack(n,m)


