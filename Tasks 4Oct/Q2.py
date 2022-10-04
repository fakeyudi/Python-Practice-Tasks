# Q. int arr[]={-1,2,-3,4,-5,6}
# I need positives on left and negatives on right, given ordering of elements not required
# eg : {-1,2,1}
# output {2,1,-1}

arr = [-1,2,-3,4,-5,6]
arr.sort(reverse=True)
print(arr)