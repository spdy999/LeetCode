/*
 * @lc app=leetcode id=70 lang=cpp
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution
{
public:
    int climbStairs(int n)
    {
        // Bottom-Up Tabulation
        map<int, int> memo;
        memo[1] = 1;
        memo[2] = 2;

        if (n == 1)
            return memo[1];
        if (n == 2)
            return memo[2];

        int cal = 0;
        for (int i = 3; i <= n; i++) // O(n)
        {
            cal = memo[i - 1] + memo[i - 2];
            memo[i] = cal;
        }
        return memo[n]; // O(1)
    }
};
// @lc code=end
