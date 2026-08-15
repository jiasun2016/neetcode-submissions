class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                # 左边是短板，处理 left 指针
                if height[left] >= left_max:
                    left_max = height[left]  # 更新左侧最大值，此位置无法蓄水
                else:
                    res += left_max - height[left]  # 确定 left_max 为瓶颈，计算蓄水量
                left += 1  # 移动指针
            else:
                # 右边是短板，处理 right 指针
                if height[right] >= right_max:
                    right_max = height[right]  # 更新右侧最大值，此位置无法蓄水
                else:
                    res += right_max - height[right]  # 确定 right_max 为瓶颈，计算蓄水量
                right -= 1  # 移动指针
                
        return res