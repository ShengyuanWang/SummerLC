# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的
# 功能。(若队列中没有元素，deleteHead 操作返回 -1 ) 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#  
# 
#  示例 2： 
# 
#  输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
#  
# 
#  提示： 
# 
#  
#  1 <= values <= 10000 
#  最多会对 appendTail、deleteHead 进行 10000 次调用 
#  
#  Related Topics 栈 设计 队列 👍 525 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class CQueue:
    '''
    建立两个stack，一个输入一个输出，处于输入栈底部元素为输出栈栈顶
    '''

    def __init__(self):
        self.stk1 = []
        self.stk2 = []


    def appendTail(self, value: int) -> None:
        self.stk1.append(value)



    def deleteHead(self) -> int:
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
        if not self.stk2:
            return -1
        else:
            return self.stk2.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
# leetcode submit region end(Prohibit modification and deletion)
