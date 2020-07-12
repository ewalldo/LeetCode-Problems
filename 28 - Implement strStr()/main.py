class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size_h = len(haystack)
        size_n = len(needle)
        count = 0
        
        if needle == "":
            return 0
        
        if size_n > size_h:
            return -1
        
        for i in range(size_h):
            if haystack[i] == needle[count]:
                count = count + 1
                while (count < size_n and (i + count) < size_h):
                    if haystack[i + count] == needle[count]:
                        count = count + 1
                    else:
                        count = 0
                        break
                if count >= size_n:
                    return i
            else:
                count = 0
        return -1
