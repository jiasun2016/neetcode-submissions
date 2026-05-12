class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:  # 总牌数不能被 groupSize 整除，直接失败
            return False
        
        count = collections.Counter(hand)  # 统计每张牌出现次数
        hand.sort()  # 从小到大排序，保证从最小牌开始组
        
        for num in hand:
            if count[num]:  # 如果这张牌还没用完，可以作为一组的起点
                
                # 尝试构建连续 groupSize 张牌
                for i in range(num, num + groupSize):
                    
                    if not count[i]:  # 如果某张牌不存在，无法构成连续组
                        return False
                    
                    count[i] -= 1  # 使用这张牌
        
        return True
