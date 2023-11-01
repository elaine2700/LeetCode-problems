class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        
        if len(image) == 0:
            return image
        currentColor = image[sr][sc]
        if currentColor == color:
            return image
        numRows = len(image)
        numCols = len(image[0])
        unvisited = [(sr, sc)]

        while unvisited:
            #change current
            currRow, currCol = unvisited.pop()
            #set current new Color
            image[currRow][currCol] = color

            #Check if color is the same
            #check top
            if currRow > 0:
                if image[currRow - 1][currCol] == currentColor:
                    unvisited.append((currRow - 1, currCol))        
            #check right
            if currCol < numCols-1:
                if image[currRow][currCol + 1] == currentColor:
                    unvisited.append((currRow, currCol + 1))
            #check bottom
            if currRow < numRows - 1:
                if image[currRow + 1][currCol] == currentColor:
                    unvisited.append((currRow + 1, currCol))
            #check left
            if currCol > 0:
                if image[currRow][currCol - 1] == currentColor:
                    unvisited.append((currRow, currCol - 1))
    
        return image

run_program = Solution()
newList = run_program.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2)
print(newList)