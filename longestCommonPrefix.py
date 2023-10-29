class Solution:
    def longestCommonPrefix(self, strs):
        pointer = 0
        first_string = strs[0]
        currentChar = first_string[pointer]
        while currentChar != None:
            currentChar = first_string[pointer]
            print("Comparing {}".format(currentChar))
            #for each s in string
            for word in strs:
                if pointer >= len(word) or word[pointer] != currentChar:
                    currentChar = None
                    return first_string[:pointer]
                    #return first_string[:pointer]
            #point next position
            pointer += 1    
        return first_string[:pointer]
        # string prefix is the substring of the first string[0:pointer]

prefix_solution = Solution()
print(prefix_solution.longestCommonPrefix(["flower", "flower", "flower"]))



