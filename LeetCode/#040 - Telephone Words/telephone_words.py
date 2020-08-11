## UPER ##
# Recieve String of numbers
# return array of string values
    # values are based on letters mapped to each number
# as no limit to input, ITERATIVE NOT SUITABLE
# RECURSION
    # base condition = no more combinations
    # return to base = add combo, then remove it (so not repeated)






class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        output = []
        
        def recursive_helper(current_combo, remaining_digits):
            if len(remaining_digits) == 0:
                output.append(current_combo)
                
            else:
                letters = keypad[remaining_digits[0]]
                for letter in letters:
                    new_combo = current_combo + letter
                    recursive_helper(new_combo, remaining_digits[1:])
                
        if digits:
            recursive_helper("", digits)
            
        return output