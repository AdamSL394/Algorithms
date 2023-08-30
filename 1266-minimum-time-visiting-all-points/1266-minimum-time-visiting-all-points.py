class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        i,j = 0,1
        diff = 0
        for index, (x, y) in enumerate(points[1:], 1):
            diff += max(abs(points[index - 1][i] - points[index][i]), abs(points[index-1][j] -  points[index][j]))
        return diff