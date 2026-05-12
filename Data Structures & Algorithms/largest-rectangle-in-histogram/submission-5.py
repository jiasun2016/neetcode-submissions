class Solution:
   
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  
        for i, h in enumerate(heights):
            start = i  
            # start：假设当前高度 h 只能从自己 i 开始（保守左边界）
            while stack and stack[-1][1] > h:
                # 如果栈顶柱子比当前柱子高：
                # 说明栈顶柱子「右边界」被当前 i 卡住了
                index, height = stack.pop()
                # index：这个 height 能延伸到的最左位置 不是 height的index
                maxArea = max(maxArea, height * (i - index))
                # 面积计算：
                # 左边界 = index
                # 右边界 = i（当前柱子）
                # 宽度 = i - index
                start = index
                # 当前高度 h 继承被弹出柱子的左边界
                # 因为：它们比 h 高，能站住的地方 h 也能站

            stack.append((start, h))
            # 把当前柱子入栈
            # 它的左边界可能已经被 while 扩展到更左

        # 处理栈里剩余的柱子（它们右边没有更矮的了）
        n = len(heights)
        for index, height in stack:
            maxArea = max(maxArea, height * (n - index))
            # 右边界 = n

        return maxArea
