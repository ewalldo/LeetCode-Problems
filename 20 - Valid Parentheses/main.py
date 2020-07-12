class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        size_stack = 0
        size_ = len(s)
        for i in range(size_):
            if s[i] == "(":
                stack.append('(')
                size_stack = size_stack + 1
            elif s[i] == "[":
                stack.append('[')
                size_stack = size_stack + 1
            elif s[i] == "{":
                stack.append('{')
                size_stack = size_stack + 1
            elif s[i] == ")":
                if size_stack == 0:
                    return False
                c = stack.pop()
                if c == '(':
                    size_stack = size_stack - 1
                else:
                    return False
            elif s[i] == "]":
                if size_stack == 0:
                    return False
                c = stack.pop()
                if c == '[':
                    size_stack = size_stack - 1
                else:
                    return False
            elif s[i] == "}":
                if size_stack == 0:
                    return False
                c = stack.pop()
                if c == '{':
                    size_stack = size_stack - 1
                else:
                    return False
        if size_stack > 0:
            return False
        else:
            return True
