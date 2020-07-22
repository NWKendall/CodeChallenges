def isBalanced(s):
    """
    given string containing bracket characters
    populate stack from string
        - open brackets
    check vals in string against last item in stack (open bracket)
        - if closing bracket matches
            -pop from stack
        - otherwise return "NO"
    return "YES" if balanced, "NO" if unbalanced


    EDGE / CONTROL CASES
    1) Empty stack
    2) stack has odd length

    TESTS 4,5,9 FAILING!
    """

    # open/closed brackets share the same indeces for logic checks
    open_brackets = ("(", "{", "[", "|")
    closed_brackets = (")", "}", "]", "|")
    # need stack to store characs
    stack = []

    for bracket in s:
        # need to populate stack with open brackets
        if bracket in open_brackets:
            stack.append(bracket)

        # so we can pop them from stack if pair is found
        elif bracket in closed_brackets:

            # control for empty stack
            if len(stack) == 0:
                return "NO"
            
            # get last value from stack to check for pair
            pop_val = stack[-1]

            # gets indeces from bracket sets above
            stack_check = open_brackets.index(pop_val)
            bracket_check = closed_brackets.index(bracket)
            
            # popping if indeces match
            if bracket_check == stack_check:
                stack.pop()

            # otherwise control for non matches / odd length of stack
            else:
                return "NO"
    
    # brackets are balanced if reaches here
    return "YES"