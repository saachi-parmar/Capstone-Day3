# ----------------------------------------------------------------------------------
# MERGE SORT -----------------------------------------------------------------------

def merge_sort(arr):
    if  len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
    
        i = j = k = 0
        # write your code here
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i+=1
            else:
                arr[k] = right_half[j]
                j+=1
            k += 1
            
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    
queue = [40, 30, 10, 20]
print("Original Queue: ", queue)
    
merge_sort(queue)
print("Sorted Queue Using Merge Sort: ", queue)


#-------------------------------------------------------------------------------------
# Quick Sort -------------------------------------------------------------------------
def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr [len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quick_sort(left) + middle + quick_sort(right)
    
queue = [40, 20, 30, 20]
print("Original Queue:", queue)
    
sorted_queue = quick_sort(queue)
print("Sorted Queue Using Quick Sort:",sorted_queue)        
        
