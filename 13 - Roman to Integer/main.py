class Solution:
    def romanToInt(self, s: str) -> int:
        out_value = 0
        size_inp = len(s)
        flag = False
        for i in range(size_inp):
            if flag == False:
                if s[i] == "V":
                    out_value  = out_value + 5
                elif s[i] == "L":
                    out_value  = out_value + 50
                elif s[i] == "D":
                    out_value  = out_value + 500
                elif s[i] == "M":
                    out_value  = out_value + 1000
                elif s[i] == "I":
                    if i + 1 < size_inp:
                        if s[i+1] == "V":
                            out_value = out_value + 4
                            flag = True
                        elif s[i+1] == "X":
                            out_value = out_value + 9
                            flag = True
                        else:
                            out_value = out_value + 1
                    else:
                        out_value = out_value + 1
                elif s[i] == "X":
                    if i + 1 < size_inp:
                        if s[i+1] == "L":
                            out_value = out_value + 40
                            flag = True
                        elif s[i+1] == "C":
                            out_value = out_value + 90
                            flag = True
                        else:
                            out_value = out_value + 10
                    else:
                        out_value = out_value + 10
                elif s[i] == "C":
                    if i + 1 < size_inp:
                        if s[i+1] == "D":
                            out_value = out_value + 400
                            flag = True
                        elif s[i+1] == "M":
                            out_value = out_value + 900
                            flag = True
                        else:
                            out_value = out_value + 100
                    else:
                        out_value = out_value + 100
            else:
                flag = False
        return out_value
