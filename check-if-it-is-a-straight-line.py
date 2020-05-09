from sys import maxsize


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (len(coordinates) < 2):
            return False
        else:
            (a, b), (c, d) = coordinates[0], coordinates[1]
            if (len(coordinates) > 2):
                if (c - a != 0):
                    slope = (d - b)/(c - a)
                    def lineEq(x, y): return (y - b) - slope * (x - a)
                else:
                    slope = maxsize
                    def lineEq(x): return x - a

                for pnt in coordinates[2:]:
                    if (not self.isPntOnTheLine(pnt, lineEq, slope)):
                        return False

                return True
            else:
                return True

    def isPntOnTheLine(self, pnt, lineEq, slope):
        if (slope != maxsize):
            return lineEq(pnt[0], pnt[1]) == 0
        else:
            return lineEq(pnt[0]) == 0
