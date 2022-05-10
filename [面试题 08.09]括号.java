//括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。 
//
// 说明：解集不能包含重复的子集。 
//
// 例如，给出 n = 3，生成结果为： 
//
// 
//[
//  "((()))",
//  "(()())",
//  "(())()",
//  "()(())",
//  "()()()"
//]
// 
// Related Topics 字符串 动态规划 回溯 👍 112 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    List<String> res = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        String str = "";
        dfs(n, n, str);
        return res;
    }

    public void dfs(int left, int right, String s) {
        if (left == 0 && right == 0) {
            res.add(new String(s));
            return;
        }
        if (left < 0 || right < 0|| left > right) {
            return;
        }
        dfs(left-1, right, s+"(");
        dfs(left, right-1, s+")");
    }
}
//leetcode submit region end(Prohibit modification and deletion)
