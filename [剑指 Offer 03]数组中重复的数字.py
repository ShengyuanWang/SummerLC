# 找出数组中重复的数字。 
# 
#  
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
# 找出数组中任意一个重复的数字。 
# 
#  示例 1： 
# 
#  输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3 
#  
# 
#  
# 
#  限制： 
# 
#  2 <= n <= 100000 
#  Related Topics 数组 哈希表 排序 👍 828 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        '''
        change the position of two num if num in 0---n-1, if the same then return
        '''
        for i, num in enumerate(nums):
            while i != num:
                if num == nums[num]:
                    return num
                nums[i], nums[num] = nums[num], nums[i]
                num = nums[i]
        return -1

# leetcode submit region end(Prohibit modification and deletion)
'''
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        """
        先排序，相同数字聚集在一起，然后比较i和i+1
        """
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        return -1
'''

'''
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        """
        hashmap, find the amount of num in the list, if num = 2, then retunr
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                if dic[num] == 1:
                    return num
        return -1
'''