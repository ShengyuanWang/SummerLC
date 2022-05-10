//数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
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
// Related Topics 字符串 动态规划 回溯 👍 2631 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    List<String> result = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        String str = "";
        dfs(n, n, str);
        return result;
    }

    public void dfs(int left, int right, String s) {
        if (left == 0 && right == 0) {
            result.add(s);
            return;
        }

        if (left < 0 || right < 0 || left > right) {
            return;
        }

        dfs(left-1, right, s+"(");
        dfs(left, right-1, s+")");
    }
}
//leetcode submit region end(Prohibit modification and deletion)
