#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()
        memo[1] = 1
        memo[2] = 2

        def fib(n):
            if n == 1:
                return memo[1]
            if n == 2:
                return memo[2]
            

            print("check memo(", n, "): ", memo.get(n))
            if memo.get(n) != None:
                print("memo! ", n,  ": ",   memo)
                return memo[n]

            memo[n] = fib(n - 2) + fib(n - 1)
            print(n, memo)
            print('----------------')
            return memo[n]

        return fib(n);


        
# @lc code=end

