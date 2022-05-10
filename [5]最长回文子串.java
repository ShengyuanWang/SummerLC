//给你一个字符串 s，找到 s 中最长的回文子串。 
//
// 
//
// 示例 1： 
//
// 
//输入：s = "babad"
//输出："bab"
//解释："aba" 同样是符合题意的答案。
// 
//
// 示例 2： 
//
// 
//输入：s = "cbbd"
//输出："bb"
// 
//
// 
//
// 提示： 
//
// 
// 1 <= s.length <= 1000 
// s 仅由数字和英文字母组成 
// 
// Related Topics 字符串 动态规划 👍 5194 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String longestPalindrome(String s) {
        int maxlength = 0;
        int left = 0, right = 0;
        boolean[][] dp = new boolean[s.length()][s.length()];
        for (int i = s.length()-1; i >= 0 ; i--) {
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    if (j - i <= 1) {
                        dp[i][j] = true;
                    } else if (dp[i+1][j-1]) {
                        dp[i][j] = true;
                    }
                }
                if (dp[i][j] && j-i+1 > maxlength) {
                    maxlength = j-i+1;
                    left = i;
                    right = j;
                }
            }

        }
        return s.substring(left, right+1);
    }
}
// dp方法
// 确定 dp[i][j]的含义 -》 [i, j]闭区间是不是回文字符串
// s[i] != s[j] -> false
// s[i] == s[j]: 如果 i = j， 那一定是true，没有什么问题； 如果 i， j相差1，那么也是true， 其他情况那就需要看dp[i+1][j-1]
// 从左到右从下到上dp
//leetcode submit region end(Prohibit modification and deletion)
class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            String s1 = palindrome(s, i, i);
            String s2 = palindrome(s, i, i+1);
            res = res.length() > s1.length() ? res : s1;
            res = res.length() > s2.length() ? res : s2;
        }
        return res;

    }

    public String palindrome(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return s.substring(l+1, r);
    }
}
//双指针方法