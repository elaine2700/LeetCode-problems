class Solution(object):
    def reverseWords(self, s):
        start = -1
        space_index = -1
        reverse_s = ''
        while space_index < len(s):
            if space_index == len(s) - 1 or s[space_index] == ' ':
                word_end = space_index - 1
                temp_word = ''
                if space_index == len(s) - 1:
                    word_end = space_index
                while start < word_end:
                    temp_word = temp_word + s[word_end]
                    word_end -= 1
                start = space_index
                reverse_s += temp_word
                if space_index < len(s) - 1:
                    reverse_s += ' '
            space_index += 1
            
        return reverse_s

run_program = Solution()
reversed_word = run_program.reverseWords('hello world !-')
print(reversed_word)
