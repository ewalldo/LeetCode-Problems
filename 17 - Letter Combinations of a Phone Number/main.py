class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ["a", "b", "c"],
                '3': ["d", "e", "f"],
                '4': ["g", "h", "i"],
                '5': ["j", "k", "l"],
                '6': ["m", "n", "o"],
                '7': ["p", "q", "r", "s"],
                '8': ["t", "u", "v"],
                '9': ["w", "x", "y", "z"]}
        
        def recursion(comb, next_):
            if len(next_) == 0:
                out_.append(comb)
            else:
                for letter in phone[next_[0]]:
                    recursion(comb + letter, next_[1:])
                    
        out_ = []
        if digits:
            recursion("", digits)
        return out_
