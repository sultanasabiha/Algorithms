def queen(k,n):
    
        for i in range(n):
            if Place(k,i):
                x[k]=i
                if k==n-1:
                    print(x)
                else:
                    queen(k+1,n)
                    x[k]=0
                

def Place(k,i):
    for j in range(k-1):
        if (x[j]==i) or (abs(x[j]-i)==abs(j-k)):
            return False
    return True
global x
x=[0]*4
queen(0,4)
