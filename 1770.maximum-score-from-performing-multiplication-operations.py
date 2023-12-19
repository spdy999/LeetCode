#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Top-Down, Memoization

        # TODO: base case, something with len(nums) and len(multipliers)

        mem = {} # [mul, num, n_l, n_r] : maxi of summ
        
        n = len(nums)
        # print(n)
        m = len(multipliers)
        
        def rec(summ: int, m_i: int, n_lr_i: List[int], indicator: int) -> int: # indicator 0 = left, 1 = right
            n_l = n_lr_i[0]
            n_r = n_lr_i[1]
            mul = multipliers[m_i]
            
            is_last_m = m_i == m - 1
            if is_last_m:
                return summ + max(mul * nums[n_l], mul * nums[n_r])

            if n_l == n_r:
                return summ + mul * nums[n_l]
            
            is_last_2_even_nums_list = n_r - n_l == 1 and n % 2 == 0
            if is_last_2_even_nums_list:
                return summ + max(mul * nums[n_l], mul * nums[n_r])

            num = nums[n_lr_i[indicator]]
            key = (mul, num, n_l, n_r)
            if key in mem:
                # print(key, mem[key])
                return mem[key]


            maxi_val, maxi_ind = max((rec(summ + mul * nums[n_l], m_i + 1, [n_l + 1, n_r], 0), 0),
                                    (rec(summ + mul * nums[n_r], m_i + 1, [n_l, n_r - 1], 1), 1))
            if maxi_ind == 0: # left
                key_l = (mul, nums[n_l], n_l + 1, n_r)
                mem[key_l] = maxi_val - summ # (2,2,1)
            else:
                key_r = (mul, nums[n_r], n_l, n_r - 1)
                mem[key_r] = maxi_val - summ
            
            # print(summ, mem)
            
            return maxi_val


        n_l = 0
        n_r = n - 1
        return max(rec(0, 0, [n_l, n_r], 0), # last arg : 0 = left
                    rec(0, 0, [n_l, n_r], 1)) # last arg : 1 = right


        
# @lc code=end

