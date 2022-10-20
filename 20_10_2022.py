#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)-1
        f = -1
        for i in range(l):
            if f==-1 and nums[i]==nums[i+1]:
                f = i
            elif f!=-1 and nums[i]!=nums[i+1]:
                nums[f+1]=nums[i+1]
                f+=1
        if f==-1:
            return l+1
        return f+1
