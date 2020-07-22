class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ["(", "{", "["]
        closed_brackets = [")", "}", "]"]
        
        for char in s:
            if char in open_brackets:
                stack.append(char)
                
            elif char in closed_brackets:
                
                if len(stack) == 0:
                    return False
                
                stack_head = stack[-1]
                
                open_check = open_brackets.index(stack_head)
                closed_check = closed_brackets.index(char)
                
                if open_check == closed_check:
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            return False
        else:
            return True