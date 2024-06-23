class Solution(object):
    def twoSum(self, nums, target):

        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


# Примеры использования:
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Вывод: [0, 1]
print(sol.twoSum([3, 2, 4], 6))       # Вывод: [1, 2]
print(sol.twoSum([3, 3], 6))
print(sol.twoSum([3,5,9,7],12))