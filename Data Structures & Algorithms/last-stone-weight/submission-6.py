class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)

        for s in stones:
            bucket[s] += 1

        first = maxStone

        while first > 0:

            # 找最大存在
            while first > 0 and bucket[first] == 0:
                first -= 1

            if first == 0:
                return 0

            # 如果偶数，直接消掉
            if bucket[first] % 2 == 0:
                bucket[first] = 0
                continue

            # 找 second
            second = first - 1
            while second > 0 and bucket[second] == 0:
                second -= 1

            if second == 0:
                return first

            # smash
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1

            # reset scan hint
            first = max(first, second, first - second)

        return first