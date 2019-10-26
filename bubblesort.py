def sort(arr):
    while True:
        corrected = False
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                #Ξεσχολιάστε την παρκάτω γραμμή για να δείτε τα βήματα κατά τη διάρκεια της ταξινόμησης
                #print(arr)
                corrected = True
        if not corrected:
            return arr

#Καλύτερο Σενάριο O(n)
print(sort([1,2,3,4,5,6,7,8,9]))

#Καλύτερο Σενάριο Average O(n^2)
print(sort([7,5,3,4,8,2,6,1,9]))

#Χειρότερο Σενάριο O(n^2)
print(sort([9,8,7,6,5,4,3,2,1]))
