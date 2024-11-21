# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/?envType=daily-question&envId=2024-11-21

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0: Open, 1: Guard, 2: Wall
        boards = [[0] * n for _ in range(m)]

        guarded = set()

        for wall in walls:
            boards[wall[0]][wall[1]] = 2
        for guard in guards:
            boards[guard[0]][guard[1]] = 1

        for x in range(m):
            blocked = False
            for y in range(n):
                if boards[x][y] == 2:
                    blocked = False
                elif boards[x][y] == 1:
                    blocked = True
                elif blocked:
                    guarded.add((x, y))

            blocked = False
            for y in range(n - 1, -1, -1):
                if boards[x][y] == 2:
                    blocked = False
                elif boards[x][y] == 1:
                    blocked = True
                elif blocked:
                    guarded.add((x, y))

        for y in range(n):
            blocked = False
            for x in range(m):
                if boards[x][y] == 2:
                    blocked = False
                elif boards[x][y] == 1:
                    blocked = True
                elif blocked:
                    guarded.add((x, y))

            blocked = False
            for x in range(m - 1, -1, -1):
                if boards[x][y] == 2:
                    blocked = False
                elif boards[x][y] == 1:
                    blocked = True
                elif blocked:
                    guarded.add((x, y))

        total = m * n
        checkSum = len(walls) + len(guards)

        return total - checkSum - len(guarded)



# class Solution:
#     def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
#         # 0: Open, 1: Guard, 2: Wall
#         result = m * n

#         boards = [[0] * n for _ in range(m)]

#         for wall in walls:
#             boards[wall[0]][wall[1]] = 2
#             result -= 1

#         for guard in guards:
#             xIdx = guard[0]
#             yIdx = guard[1]
#             if boards[xIdx][yIdx] == 0:
#                 boards[xIdx][yIdx] = 1
#                 result -= 1

            
#             while xIdx >= 0:
#                 if boards[xIdx][yIdx] == 2:
#                     break
#                 if boards[xIdx][yIdx] == 0:
#                     result -= 1
#                 boards[xIdx][yIdx] = 1
#                 xIdx -= 1
            
#             xIdx = guard[0]
#             yIdx = guard[1]

#             while yIdx >= 0:
#                 if boards[xIdx][yIdx] == 2:
#                     break
#                 if boards[xIdx][yIdx] == 0:
#                     result -= 1
#                 boards[xIdx][yIdx] = 1
#                 yIdx -= 1
            
#             xIdx = guard[0]
#             yIdx = guard[1]

#             while xIdx < m:
#                 if boards[xIdx][yIdx] == 2:
#                     break
#                 if boards[xIdx][yIdx] == 0:
#                     result -= 1
#                 boards[xIdx][yIdx] = 1
#                 xIdx += 1
            
#             xIdx = guard[0]
#             yIdx = guard[1]

#             while yIdx < n:
#                 if boards[xIdx][yIdx] == 2:
#                     break
#                 if boards[xIdx][yIdx] == 0:
#                     result -= 1
#                 boards[xIdx][yIdx] = 1
#                 yIdx += 1

#         return result
