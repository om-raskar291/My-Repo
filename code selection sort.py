def selectionSort(ar):
    l = len(ar)
    
    for i in range(l-1):
        min = i
        for j in range(i+1, l-1):
            if ar[j] < ar[min]:
                min = j
        ar[i], ar[min] = ar[min], ar[i]
        
    for i in ar:
        print(i, end =' ')
    
    
    

n = int(input())
ar = [int(x) for x in input().split()[:n]]

selectionSort(ar)