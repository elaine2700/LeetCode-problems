class Solution:
    def longestPalindrome(self, s: str) -> int:
        unmatched = {}
        count = 0

        for i in range(len(s)):
            if s[i] in unmatched:
                count += 2
                unmatched.pop(s[i])
                print(unmatched)
                print(count)
            else:
                unmatched[s[i]] = 1
                print(unmatched)
                print(count)
        
        if len(unmatched) >= 1:
            count += 1
        return count

run_program = Solution()
#print(run_program.longestPalindrome('aaabbbc'))
#print(run_program.longestPalindrome('edfed'))
print(run_program.longestPalindrome('abccccdd'))