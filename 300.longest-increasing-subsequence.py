#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start
# Neetcode
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        # O(n^2)
        for i in range(len(nums) - 1, -1, -1):  # O(n)
            for j in range(i + 1, len(nums)):  # O(n)
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        # print(LIS) # [2, 2, 4, 3, 3, 2, 1, 1]
        return max(LIS)

    # def cntDepth(lst: List[int], depth: int, prev: int, adjacent: bool):

    #     # print(lst, depth, prev, adjacent)
    #     if len(lst) == 1:
    #         if lst[0] < prev:
    #             print("len(lst) == 1, if: ", lst, depth, prev, adjacent)
    #             return depth
    #         else:
    #             print("len(lst) == 1, else: ", lst, depth + 1, prev, adjacent)
    #             return depth + 1

    #     if lst[0] <= prev:
    #         # return max(
    #         #     depth, max([cntDepth(lst[1:], depth, prev) for x in lst[1:]])
    #         # )
    #         # return depth
    #         print("lst[0] <= prev", lst, depth, prev, adjacent)
    #         return max(depth, cntDepth(lst[1:], depth, prev, False))
    #     elif not adjacent and lst[0] > prev:
    #         print("lst[0] > prev", lst, depth, prev, adjacent)
    #         return max(depth, cntDepth(lst[1:], depth, prev, False))

    #     print("big return", lst[1:], depth + 1, prev, adjacent)
    #     return max([cntDepth(lst[1:], depth + 1, x, False) for x in lst])

    # return cntDepth(nums, 0, 0, True)


# @lc code=end
