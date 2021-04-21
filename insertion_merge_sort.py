#Insertion Sort
def insertion_sort(listA):
    
    for i in range(1,len(listA)):
        val_to_sort = listA[i]
        
        while listA[i-1] > val_to_sort and i > 0:
            listA[i-1],listA[i] = listA[i],listA[i-1]
            i = i-1
    return listA

#Merge Sort Using Recursion
def merge_sort(listA):
    if len(listA) > 1:
        mid = len(listA)//2
        
        L = listA[:mid]
        R = listA[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                listA[k] = L[i]
                i += 1
            else:
                listA[k] = R[j]
                j += 1
            k += 1
    
        while i < len(L):
            listA[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            listA[k] = R[j]
            j += 1
            k += 1
            
        return listA
    
print(insertion_sort([674,785,654,978,425,876,543,987]))  

print(merge_sort([674,785,654,978,425,876,543,987]))
