def sort_nums(numbers):
    numbers.sort()
    return numbers
def moveNegative(nums):
    negatives = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[negatives], nums[i] = nums[i], nums[negatives]
            negatives = negatives + 1
    return nums
    
def first_missing_positive(numbers):
 count=0
 sorted_numbers=sort_nums(numbers)
 final= moveNegative(sorted_numbers) 
 for i in range(len(final)):
    if(final[i]>0 and final[i]!= i+1):
       return i+1
    
 for i in range(len(final)):
          
          if(final[i]>0):
             count = count+1 
 return count+1

    
        
result =first_missing_positive([1,2, 3,4,5,0,-5,-6])
print(result)