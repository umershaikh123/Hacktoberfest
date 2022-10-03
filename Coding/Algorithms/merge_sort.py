def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        lptr=rptr=arrptr=0
        while lptr<len(left) and rptr<len(right):
            if left[lptr]<right[rptr]:
                arr[arrptr]=left[lptr]
                lptr+=1
            else:
                arr[arrptr]=right[rptr]
                rptr+=1
            arrptr+=1
        while lptr<len(left):
            arr[arrptr]=left[lptr]
            lptr+=1
            arrptr+=1
        while rptr<len(right):
            arr[arrptr]=right[rptr]
            rptr+=1
            arrptr+=1

arr=[12,5,4,6,1,8]
mergesort(arr)
print(arr)