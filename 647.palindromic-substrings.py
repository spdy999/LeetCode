#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:


    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = [0]

        def checkPd(il: int, ir: int, lenPd: int):
            while il >= 0 and ir < n and s[il] == s[ir]:
                cnt[0] += 1

                il -= 1
                ir += 1

        for i in range(n):
            # odd length
            checkPd(i, i, 1)

            # even length
            checkPd(i, i + 1, 2)

        return cnt[0]
        
# @lc code=end
