def merge(arr, left, mid, right):
    temp = []
    low = left
    high = mid + 1

    while low <= mid and high <= right:
        if arr[low] <= arr[high]:
            temp.append(arr[low])
            low += 1
        else:
            temp.append(arr[high])
            high += 1
    
    """
    adding the remained elements from the left sub array to 
    temp array
    """
    while low <= mid:
        temp.append(arr[low])
        low += 1
        
    """
    adding the remained elements from the right sub array to 
    temp array
    """
    while high <= right:
        temp.append(arr[high])
        high += 1
        
    i = left
    while i <= right:
        arr[i] = temp[i - left]
        i += 1


def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)


if __name__ == "__main__":

    arr = [2, 1, 4, 5, 3, 1, 9, 2]
    n = len(arr)
    merge_sort(arr, 0, n - 1)

    for i in arr:
        print(i, end=" ")
