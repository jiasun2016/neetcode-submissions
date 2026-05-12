
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A)
        # 这里l <= r work count-based binary search
        # 因为合法分割一定存在，且一定在 [0, len(A)] 内
        while l <= r:
            i = (l + r) // 2  # i 表示：A 左边取 i 个元素
            # 保证：A 左边 + B 左边 = half
            j = half - i # j 表示：B 左边取 j 个元素
            # A 左边最大值
            # 如果 i == 0，说明 A 左边不取任何元素，用 -∞ 兜底
            Aleft = A[i - 1] if i > 0 else float("-inf")
            # A 右边最小值
            # 如果 i == len(A)，说明 A 右边没有元素，用 +∞ 兜底
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
