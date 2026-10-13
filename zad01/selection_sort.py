def selection(arr):
    length=len(arr)
    for x in range(length-1):
        minI=x
        for y in range(x+1,length):
            if(arr[y]<arr[minI]):
                minI=y

        arr[minI],arr[x]=arr[x],arr[minI]
    return arr