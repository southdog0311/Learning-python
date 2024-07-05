def binary_search(arr:list, target)->int:
    low = 0
    upper = len(arr) - 1
    while low <= upper:
        mid = (low + upper) // 2  # 得到中間索引
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            upper = mid - 1
        else:
            return mid  # 找到目標值，返回它的索引
    return -1


