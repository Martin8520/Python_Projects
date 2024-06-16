class Solution:
    def largestPerimeter(self, nums):
        nums.sort()
        total_sum = 0
        ans = -1

        for num in nums:
            if num < total_sum:
                ans = num + total_sum
            total_sum += num

        return ans


sol = Solution()

print(sol.largestPerimeter([2, 1, 2]))  # Output: 5
print(sol.largestPerimeter([5, 5, 5]))  # Output: 15
print(sol.largestPerimeter([1, 12, 1, 2, 5, 50, 3]))  # Output: 12
print(sol.largestPerimeter([5, 5, 50]))  # Output: -1
