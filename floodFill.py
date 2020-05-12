class Solution:
    def __init__(self):
        self.visited = []

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        return self.floodFillHelper(sr, sc, image[sr][sc], newColor, image)

    def floodFillHelper(self, r, c, sourceClr, newClr, image):
        if (r < 0 or c < 0):
            return
        if (r >= len(image) or c >= len(image[0])):
            return
        if (sourceClr != image[r][c]):
            return
        image[r][c] = newClr

        neighbours = self.findNeighbours(r, c)

        for n in neighbours:
            if n not in self.visited:
                self.visited.append(n)
                self.floodFillHelper(n[0], n[1], sourceClr, newClr, image)

        return image

    def findNeighbours(self, r, c):
        return [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
