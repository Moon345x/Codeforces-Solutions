def binary_search(arr, target):

    left, right = 0, len(arr) - 1
    result = -1  
    
    while left <= right:
        mid = (left + right) // 2
        

        if arr[mid] <= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
q=int(input())
for i in range(q):
    m=int(input())
    print(binary_search(arr,m)+1)
