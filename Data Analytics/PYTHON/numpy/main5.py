#SEARCH, SORT, FILTER of ARRAYS
import numpy as np

arr=np.array([1,2,3,4,5,6,7])
arr1= np.array([[25, 56, 66, 23 ,56 ,77]])

arr2= np.array([[15, 86, 96],[13 ,26 ,47]])

print(np.sort(arr1)) #[[23 25 56 56 66 77]]

print(np.min(arr1)) #23
print(np.max(arr1)) #77
print(np.sum(arr1)) #253
print(np.mean(arr1)) #43.833333333333336
print(np.std(arr1)) #19.02654089074088
print(np.var(arr1)) #361.99999999999994
print(np.percentile(arr1, 50)) #56