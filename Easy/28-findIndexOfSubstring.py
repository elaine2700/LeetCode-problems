class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.find(needle)
        return -1
    
run_program = Solution()
print(run_program.strStr("sadbutsad", "sad"))
print(run_program.strStr("leetcode", "leeto"))