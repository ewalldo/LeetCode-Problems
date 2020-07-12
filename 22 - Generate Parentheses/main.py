class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        
        out_ = []
        def recursion(s = '', left = 0, right = 0):
            if len(s) == 2 * n:
                out_.append(s)
                return
            if left < n:
                recursion(s + '(', left+1, right)
            if right < left:
                recursion(s + ')', left, right+1)
                
        recursion()
        return out_
