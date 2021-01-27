
from heapq import heapify, heappush, heappop
'''
You are a hiker preparing for an upcoming hike.
 You are given heights, a 2D array of size rows x columns, 
 where heights[row][col] represents the height of cell (row, col). 
 You are situated in the top-left cell, (0, 0), 
 and you hope to travel to the bottom-right cell,
 (rows-1, columns-1) (i.e., 0-indexed).
You can move up, down, left, or right, and you wish to find a route
 that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between
 two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to
 the bottom-right cell.
'''
class Solution:

    def __init__(self, heights):
        self.heights = heights
        self.found = False
        self.solution = 0
        self.visited = set()
        self.heap = []

    def hike(self, i,j,heights,maxdiff, h):
        if self.found == True:
            return
        row = len(heights)
        col = len(heights[0])
        if i == row-1 and j == col-1:
            self.found = True
            self.solution = maxdiff
            return
        for option in self.get_options(i,j,row,col,heights):
            heappush(h,option)
        while(len(h) != 0):
            option = heappop(h)
            if (option[1],option[2]) in self.visited:
                continue
            self.visited.add((option[1],option[2]))
            self.hike(option[1],option[2], heights, option[0], h)

    def get_options(self,i,j, row, col, heights):
        options = []
        if i + 1 < row:
            diff = abs(heights[i][j]-heights[i+1][j])
            options.append((diff,i+1, j))
        if i - 1 > 0:
            diff = abs(heights[i][j]-heights[i-1][j])
            options.append((diff,i-1, j))
        if j + 1 < col:
            diff = abs(heights[i][j] - heights[i][j+1])
            options.append((diff,i,j+1))
        if j - 1 > 0:
            diff = abs(heights[i][j]-heights[i][j-1])
            options.append((diff,i,j-1))
        return options
    
    def solve(self):
        self.hike(0,0,self.heights, 0,self.heap)
        return self.solution

heights = [[1,2,2],[3,8,2],[5,3,5]]
solutionObj = Solution(heights)
print(solutionObj.solve())
