class Solution(object):
    def isHappy(self, n):
        #positive integer
        # sum of the squares of its digits
        #repeat until the number equals 1

        currentSum = n
        hash_set = list()

        while currentSum != 1 and not currentSum in hash_set:
            hash_set.append(currentSum)
            print(hash_set)

            loopSum = currentSum
            squareSum = 0

            while not loopSum == 0:
                squareSum = squareSum + pow(loopSum % 10, 2)
                loopSum = loopSum // 10

            
            currentSum = squareSum
            

        
        return currentSum == 1

run_program = Solution()
print(run_program.isHappy(19))
print("Second")
print(run_program.isHappy(2))