#Addding & Removing Elements in ARRAYS
import numpy as np

arr1= np.array([[25, 56, 66],[23 ,56 ,77]])
arr2= np.array([[15, 86, 96],[13 ,26 ,47]])

#for adding we use insert & append
#insert me specific location me add krskte hn or append me last me

#np.insert(arrayNAME, index(0,1,2), insert the value)
#np.append(arrNAME, enter the valune)

arr=np.array([1,2,3,4,5,6,7])

print(np.append(arr, [9, 0]))  #[1 2 3 4 5 6 7 9 0]
print(np.insert(arr, 3,[9, 0]))#[1 2 3 9 0 4 5 6 7]

#np.delete(arrNAME, index)
print(np.delete(arr, 4))