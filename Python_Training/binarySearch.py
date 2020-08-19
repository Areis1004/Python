def binary_search(arr, low, high, searchData):
    if high >= low:
        mid = (high + low)//2
        if arr[mid] == searchData:
            return mid
        elif arr[mid] > searchData:
            return binary_search(arr, low, mid - 1, searchData)
        else: 
            return binary_search(arr, mid + 1, high, searchData)
    else:
        return -1




listData = [1, 10, 20, 30, 40, 45, 50, 60, 67, 69, 70, 80]

returnindex = binary_search(listData, 0, len(listData)-1, 62)

print(f"Value Foundd at index {returnindex}")