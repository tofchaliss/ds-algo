def dutchsort(arr, mid):
    i,j = 0, 0
    k = len(arr)-1
    while j <= k:
        if arr[j] < mid:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j + 1
        elif arr[j]> mid:
            arr[j], arr[k] = arr[k], arr[j]
            k = k - 1
        else:
            j = j + 1

    return arr

if __name__ == "__main__":
    a = [1, 0, 2, 1, 0, 1]
    print(dutchsort(a, 1))

