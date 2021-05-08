def quick_sort(l):
    
    size = len(l)
    if size <= 1:
        return l
    else:
        pivot = l.pop()
    print(pivot)
    ele_greater = []
    ele_smaller = []
    
    for i in l:
        if i > pivot:
            ele_greater.append(i)
        else:
            ele_smaller.append(i)
    
    return quick_sort(ele_smaller) + [pivot] + quick_sort(ele_greater)
    
print(quick_sort([1,56,643,42,65,123,6,2,34,4]))
