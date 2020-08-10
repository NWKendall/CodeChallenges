## UPER ##
# receive string
# return string
# for every set of parenthesis, reverse it's contents
# filter out parenthesis



class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        letters = list(s)
        stack = []
               
        for i, chr in enumerate(letters):
            
            if chr == "(":
                stack.append(i)
                
            elif chr == ")":
                opener_index = stack.pop()
                
                letters[opener_index:i] = letters[i:opener_index:-1]
                
                
        return "".join(l for l in letters if l not in "()")
