# array = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#          [".", "9", "8", ".", ".", ".", ".", "6", "."],
#          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#          [".", "6", ".", ".", ".", ".", "2", "8", "."],
#          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
#
import ui


class Solve(object):
    def __init__(self, array):
        self.line = [[False] * 9 for i in range(9)]
        self.column = [[False] * 9 for i in range(9)]
        self.block = [[[False] * 9 for i in range(3)] for j in range(3)]
        self.valid = False
        self.spaces = []
        self.array = array
        print(array)

    def dfs(self, pos):
        if pos == len(self.spaces):
            self.valid = True
            return

        i, j = self.spaces[pos]
        for digit in range(9):
            if self.line[i][digit] == self.column[j][digit] == self.block[i // 3][j // 3][digit] is False:
                self.line[i][digit] = self.column[j][digit] = self.block[i // 3][j // 3][digit] = True
                self.array[i][j] = str(digit + 1)
                self.dfs(pos + 1)
                self.line[i][digit] = self.column[j][digit] = self.block[i // 3][j // 3][digit] = False
            if self.valid:
                return

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.array[i][j] == '':
                    self.spaces.append([i, j])
                else:
                    digit = int(self.array[i][j]) - 1
                    self.line[i][digit] = self.column[j][digit] = self.block[i // 3][j // 3][digit] = True

        self.dfs(0)
        print(self.array)
