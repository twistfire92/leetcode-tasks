# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        arr = [[i for i in range(1, n+1)] for _ in range(n)]

        step = 0
        cur_point = [0, n-1]
        counter = n+1

        def get_offset(step):
            return {
                0: [1, 0],
                1: [0, -1],
                2: [-1, 0],
                3: [0, 1],
            }[step % 4]

        while n-1 > 0:
            for _ in range(2):
                offset = get_offset(step)
                for _ in range(n - 1):
                    cur_point[0], cur_point[1] = cur_point[0] + offset[0], cur_point[1] + offset[1]
                    arr[cur_point[0]][cur_point[1]] = counter
                    counter += 1
                step += 1
            n -= 1

        return arr


if __name__ == '__main__':
    print(Solution().generateMatrix(5))