# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        if (lst_len := len(nums)) == 1:
            return [nums]
        for i in range(lst_len):
            bufer = nums[:]
            head = bufer.pop(i)
            tails = self.permute(bufer)
            for tail in tails:
                result.append([head] + tail)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))
