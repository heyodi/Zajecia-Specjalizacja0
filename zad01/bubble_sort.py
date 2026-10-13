def bubble(arr):
    length=len(arr)
    for i in range(length):
        for j in range(length-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
            
tab=[6,67,34,32,77,56,58]
tab_sor=bubble(tab)
print(tab_sor)