class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = len(s1)
        tempWindow = []

        while end <= len(s2):
            tempWindow = [s2[i] for i in range(start, end)]
            print(start, ' ', end)
            print(tempWindow)
            for i in range(len(s1)):
                print('current letter: ' + s1[i])

                for j in range(len(tempWindow)):
                    print(tempWindow[j])
                    if s1[i] == tempWindow[j]:
                        #match
                        #remove from tempWindow
                        print('Removing ' + tempWindow[j])
                        tempWindow.pop(j)
                        print(tempWindow)
                        if len(tempWindow) <= 0:
                            return True
                        break
            start += 1
            end+= 1
        return False

run_program = Solution()
result = run_program.checkInclusion('adc', 'dcda')
print(result)