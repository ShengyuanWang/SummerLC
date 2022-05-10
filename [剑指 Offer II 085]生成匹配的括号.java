//正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
//
// 
//
// 示例 1： 
//
// 
//输入：n = 3
//输出：["((()))","(()())","(())()","()(())","()()()"]
// 
//
// 示例 2： 
//
// 
//输入：n = 1
//输出：["()"]
// 
//
// 
//
// 提示： 
//
// 
// 1 <= n <= 8 
// 
//
// 
//
// 注意：本题与主站 22 题相同： https://leetcode-cn.com/problems/generate-parentheses/ 
// Related Topics 字符串 动态规划 回溯 👍 28 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    List<String> result = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        String str = "";
        dfs(n, n, str);
        return result;
    }

    public void dfs(int left, int right, String s) {
        if (right == 0 && left == 0) {
            result.add(new String(s));
            return;
        }
        if (left < 0 || right < 0 || right < left) {
            return;
        }
        dfs(left-1, right, s+"(");
        dfs(left, right-1, s+")");
    }
}
//leetcode submit region end(Prohibit modification and deletion)
