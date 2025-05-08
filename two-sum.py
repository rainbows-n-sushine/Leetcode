class Solution:
   def twoSum(self, num:list[int],target:int)->list[int]:
      hashTable={} #value:index activity

      for i,n in enumerate(num):
         diff=target-n
         if diff in hashTable:
            return [hashTable[diff],i]
         hashTable[n]=i
      return
   
solution=Solution()
input_list=[5,6,4,4,2,3]
target=8
result=solution.twoSum(input_list,target)
print(result)