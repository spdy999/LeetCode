#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        for i in range(2, numRows):
            last_row = ans[-1]
            gen_row = [1]
            for j in range(1, i):
                gen_row.append(last_row[j-1] + last_row[j])
                continue
            gen_row.append(1)
            ans.append(gen_row)
        
        return ans


        
# @lc code=end

