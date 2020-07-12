class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0 or numRows == 1:
            return s
        
        ret_ = []
        n = len(s)
        cycle_len = 2 * numRows - 2
        
        for i in range(numRows):
            for j in range(i, n, cycle_len):
                ret_.append(s[j])
                if i != numRows-1 and i != 0 and j + cycle_len - 2*i < n:
                    ret_.append(s[j+cycle_len-2*i])
        ret_ = "".join(ret_)
        return ret_
