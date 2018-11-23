# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(range(len(nums)-1))
        for i in range(len(nums) - 1):
            print('i :', i)
            for j in range(len(nums) - i - 1):
                print('j :', j)
                if nums[i] + nums[i + j + 1] == target:
                    return [i, i + j + 1]
        return []
        # for i in range(len(nums) - 1):
        #     print(i)


nums = [2, 7, 11, 15]
target = 9
obj = Solution()
print(obj.twoSum(nums, target))