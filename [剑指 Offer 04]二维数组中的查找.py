# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个
# 整数，判断数组中是否含有该整数。 
# 
#  
# 
#  示例: 
# 
#  现有矩阵 matrix 如下： 
# 
#  
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#  
# 
#  给定 target = 5，返回 true。 
# 
#  给定 target = 20，返回 false。 
# 
#  
# 
#  限制： 
# 
#  0 <= n <= 1000 
# 
#  0 <= m <= 1000 
# 
#  
# 
#  注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/ 
#  Related Topics 数组 二分查找 分治 矩阵 👍 660 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        '''
           以右上角为base，往左数值逐渐变小，向下数值逐渐变大
           可以看作二叉搜索树
           从右上角或者左下角搜索就可以
        '''
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >=0 and j < n:
            if matrix[i][j] == target:
                return True
            # 判断左右上下
            if matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
"""
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        '''
        大傻逼方法
        直接找
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
"""

"""
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        '''
           以右上角为base，往左数值逐渐变小，向下数值逐渐变大
           可以看作二叉搜索树
           从右上角或者左下角搜索就可以
        '''
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >=0 and j < n:
            if matrix[i][j] == target:
                return True
            # 判断左右上下
            if matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
"""