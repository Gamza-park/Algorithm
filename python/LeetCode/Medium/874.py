# https://leetcode.com/problems/walking-robot-simulation/?envType=daily-question&envId=2024-09-04
class Solution:
    def check(self, li, diff, value, isPlus) -> List[int]:
        result = []

        for val in li:
            if isPlus:
                if diff < val and val <= diff + value:
                    result.append(val)
            else:
                if diff > val and val >= diff - value:
                    result.append(val)

        return result

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        up = True
        down = False
        left = False
        right = False

        now = [0, 0]

        maxLength = -inf

        objectDataX = {}
        objectDataY = {}

        for obstacle in obstacles:
            if obstacle[0] not in objectDataX:
                objectDataX[obstacle[0]] = []
            objectDataX[obstacle[0]].append(obstacle[1])

            if obstacle[1] not in objectDataY:
                objectDataY[obstacle[1]] = []

            objectDataY[obstacle[1]].append(obstacle[0])          

        for command in commands:
            if command > 0:
                if up:
                    if now[0] in objectDataX:
                        obj = self.check(objectDataX[now[0]], now[1], command, True)
                        if len(obj) == 0:
                            now[1] += command
                        else:
                            now[1] = obj[0] - 1
                    else:
                        now[1] += command
                elif down:
                    if now[0] in objectDataX:
                        obj = self.check(objectDataX[now[0]], now[1], command, False)
                        if len(obj) == 0:
                            now[1] -= command
                        else:
                            now[1] = obj[0] + 1
                    else:
                        now[1] -= command
                elif left:
                    if now[1] in objectDataY:
                        obj = self.check(objectDataY[now[1]], now[0], command, False)
                        if len(obj) == 0:
                            now[0] -= command
                        else:
                            now[0] = obj[0] + 1
                    else:
                        now[0] -= command
                elif right:
                    if now[1] in objectDataY:
                        obj = self.check(objectDataY[now[1]], now[0], command, True)
                        if len(obj) == 0:
                            now[0] += command
                        else:
                            now[0] = obj[0] - 1
                    else:
                        now[0] += command


            elif command == -1:
                if up:
                    up = False
                    right = True
                elif down:
                    down = False
                    left = True
                elif left:
                    left = False
                    up = True
                elif right:
                    right = False
                    down = True

            elif command == -2:
                if up:
                    up = False
                    left = True
                elif down:
                    down = False
                    right = True
                elif left:
                    left = False
                    down = True
                elif right:
                    right = False
                    up = True
                    
            if maxLength < now[0] ** 2 + now[1] ** 2:
                maxLength = now[0] ** 2 + now[1] ** 2

        return maxLength
    



        
        