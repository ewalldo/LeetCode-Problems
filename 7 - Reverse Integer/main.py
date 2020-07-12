class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        out_str = ""
        if str_x[0] == "-":
            out_str = "-"
            str_x = str_x[1:]
        
        for i in range(1, len(str_x) + 1):
            out_str = out_str + str_x[-i]
        
        out_int = int(out_str)
        if out_int >= 2**31 or out_int <= -2**31:
            return 0
        else:
            return int(out_str)
