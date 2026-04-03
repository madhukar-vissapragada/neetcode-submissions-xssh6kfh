class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        a = strs[0]
        b = strs[1] 

        i = j = 0
        result = ""
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                result += a[i]
                i += 1 
                j += 1
            else:
                break 
        
        print(result)
        
        for index in range(2, len(strs)):
            i = j = 0
            a = result 
            b = strs[index]
            current_result = ""

            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    current_result += a[i]
                    i += 1 
                    j += 1
                else:
                    break 
            result = current_result 
            print(current_result)
        
        return result 



        