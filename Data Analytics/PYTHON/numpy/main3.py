#combining & spliting ARRAYs
import numpy as np

arr1= np.array([[25, 56, 66],[23 ,56 ,77]])
arr2= np.array([[15, 86, 96],[13 ,26 ,47]])

print(np.concatenate([arr1,arr2]))
print(np.hstack([arr1,arr2]))# horizontal concatenetion
print(np.vstack([arr1,arr2]))# vertical concetenation

#_SPILTING
print(arr1[0,0:1]) #0 wala ka 0 se 1 tk 
print(arr1[1,0:1])#1 wala ka 0 se 1 tk 

print("_______________________")
arr=np.array([1,2,3,4,5,6,7,7])
print(np.split(arr,4))# spilt in 4 portions