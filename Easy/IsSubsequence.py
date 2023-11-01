class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # t complete word
        # s subsequence
        # s chars in relative order as t chars
        # s len is less or equal than t len
        if len(s) < 0:
            return True
        if len(s) > len(t):
            return False
        #two pointers
        s_pointer = 0
        t_pointer = 0

        while t_pointer < len(t):
            
            if s[s_pointer] == t[t_pointer]:
                #s char in s_pointer match with t char in t_pointer
                s_pointer += 1
                t_pointer += 1
                print("sPointer:{t_}".format(t_ = t_pointer))
                print("sPointer:{s_}".format(s_ = s_pointer))
            else:
                #search in next t_pointer pos.
                t_pointer += 1
                print("sPointer:{t_}".format(t_ = t_pointer))
        
            # at the end if s_pointer is the same as len(s)
            # then all letters where found
            if s_pointer >= len(s):
                return True
        return False

program_run = Solution()
print(program_run.isSubsequence("ahd", "ahbgdc"))