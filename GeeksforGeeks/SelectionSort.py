class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        
        for i in range(n):
            min_index = i
            
            for j in range(i+1, n):
                if arr[min_index] >= arr[j]:
                    min_index = j
            # swap:
            arr[min_index], arr[i] = arr[i], arr[min_index]
            
        return arr