class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        maxRows = len(grid)
        maxCols = len(grid[0])
        maxSize = 0
        visited = [] # list of tuples (r,c)
        currentSize = 0 # list of ints (num of nodes in island)
        
        for r in range(maxRows):
            for c in range(maxCols):
                islandNodes = [(r,c)]
                if grid[r][c] == 1:    
                #if the first node not in visited list
                    if (r, c) not in visited:
                        visited.append((r,c))
                        print("finding current island size: ")
                        island = self.dfs(grid, islandNodes, maxRows, maxCols)
                        visited.append(island)
                        currentSize = len(island)
                        print("Current Size ",currentSize)
                        if currentSize > maxSize:
                            maxSize = currentSize
        print("Max Size ", maxSize)
        return maxSize
        
                    

    def dfs(self, grid, nodes, maxR, maxC):
        # function return list of visited.
        # size will be the length of visited.
        islandNodes = []
        print(nodes)
        while nodes:
            nR, nC = nodes.pop()
            # check top
            if (nR,nC) not in islandNodes:
                islandNodes.append((nR,nC))
                if nR > 0:
                    if grid[nR-1][nC] == 1:
                        print("Checking node ", nR-1, " ", nC)
                        nodes.append((nR-1, nC))
                        
                # check right
                if nC < maxC - 1:
                    if grid[nR][nC + 1] == 1:
                        print("Checking node ", nR, " ", nC + 1)
                        nodes.append((nR, nC + 1))
                # check bottom
                if nR < maxR - 1:
                    if grid[nR+1][nC] == 1:
                        print("Checking node ", nR + 1, " ", nC)
                        nodes.append((nR+1, nC))
                # check left
                if nC > 0:
                    if grid[nR][nC-1] == 1:
                        print("Checking node ", nR, " ", nC - 1)
                        nodes.append((nR,nC-1))
            print("Nodes ", nodes)
        return islandNodes

check = Solution()

maxIsland = check.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(maxIsland)