class Solution:
    def sortColors(self, nums: List[int]) -> None:
        one=[]
        two=[]
        zero=[]
        for i in range(len(nums)):
            if nums[i]==1:
                one.append(nums[i])
            elif nums[i]==2:
                two.append(nums[i])
            else:
                zero.append(nums[i])
        nums[:]=zero+one+two
        return nums       