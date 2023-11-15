# Structure for an item which stores weight and
# corresponding value of Item
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
 
# Main greedy function to solve problem
def fractionalKnapsack(W, arr):
 
    # Sorting Item on basis of ratio
 
 
    # Result(value in Knapsack)
    finalvalue = 0.0
 
    # Looping through all Items
    for item in arr:
 
        # If adding Item won't overflow,
        # add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
 
        # If we can't add current Item,
        # add fractional part of it
        else:
            finalvalue += item.value * W / item.weight
            break
     
    # Returning final value
    return finalvalue
 
 
# Driver Code
if __name__ == "__main__":
 
    W = 20
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    #arr = [Item(10, 2), Item(4, 3), Item(8, 4), Item(7,5), Item(6,6)]
    #arr = [Item(25, 18), Item(27, 15), Item(15, 10)]
    max_val=[]
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)   
    
    # Function call
    max_val.append(fractionalKnapsack(W, arr))
    print("Order by P/W:",max_val[0])
    arr.sort(key=lambda x: (x.weight), reverse=True) 
    '''for item in arr:
        print(item.value,item.weight)'''
    max_val.append(fractionalKnapsack(W, arr))
    print("Order by Weight:",max_val[1])
    arr.sort(key=lambda x: (x.value), reverse=True)  
    
    # Function call
    max_val.append(fractionalKnapsack(W, arr))
    print("Order by Profit:",max_val[2])
    # inbuilt function to find the position of minimum
    res=max(max_val)
    
    # inbuilt function to find the position of maximum
    maxpos = max_val.index(res)
    
    match maxpos:
        case 0:
            print("Maximum profit given by order by P/W approach:",res)

        case 1:
            print("Maximum profit given by order by weight approach:",res)
        case 2:
            print("Maximum profit given by order by profit approach:",res)
    


'''
  # Driver Code
if __name__ == "__main__":
 
    m = int(input("Enter Knapsack Capacity:"))
    n = int(input("Enter number of objects:"))

    w=[]*n
    p=[]*n
    res=[]*3
    arr=[[]*2]*n
    print("Enter weights for the ith object:\n")
    for i in range(n):
        arr[0][i] = int(input())

    print("Enter profits for the ith object:\n")
    for i in range(n):
        arr[i][0] = int(input())

    w,p=orderByWeight(w,p,n)  arr.sort(key=lambda x: (x.value/x.weight), reverse=True)

    w,p=orderByProfit(w,p,n)
    w,p=orderByRatio(w,p,n)

    
    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)
  '''