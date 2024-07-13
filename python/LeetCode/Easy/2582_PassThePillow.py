class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        idx = 1
        isRight = True

        cnt = 0

        maxIdx, minIdx = n, 1

        while True:
            if isRight:
                idx = idx + 1
            else:
                idx = idx - 1

            if idx == maxIdx:
                isRight = False
            elif idx == minIdx:
                isRight = True

            cnt += 1
            if time == cnt:
                break

        return idx
        