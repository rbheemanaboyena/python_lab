#time O(n^2) space O(1)
def two_num_sum(array, targetsum):
   for i in range(len(array)-1):
       firstnum = array[i]
       for j in range(i+1, len(array)):
           secondnum = array[j]
           if firstnum + secondnum == targetsum:
              return [firstnum, secondnum]
   return []

#time O(n) space O(n)
def two_num_sum1(array, targertsum):
   nums = {}
   for num in array:
      potentialmatch = targetsum - num
      if potentialmatch in nums:
         return [potentialmatch, num]
      else:
         nums[num] = True
   return []

