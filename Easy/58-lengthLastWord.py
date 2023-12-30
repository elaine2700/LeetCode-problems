class Solution(object):
    def lengthOfLastWord(self, s):
        last = 0
        count = len(s)

        foundWord = False

        # stop loop when it has found a word
        while count >= 0 and not foundWord:
            count = count - 1
            foundWord = s[count] != ' '
                
        # restart on count index
        while count >= 0 and s[count] != ' ':
            count = count - 1
            last = last + 1

        return last
    
run_program = Solution()
print(run_program.lengthOfLastWord("luffy is still joyboy"))
print(run_program.lengthOfLastWord("Hello World"))
print(run_program.lengthOfLastWord("   fly me   to   the moon  "))
print(run_program.lengthOfLastWord("a"))