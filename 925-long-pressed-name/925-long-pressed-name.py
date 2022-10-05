class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):return False
        i = j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif i > 0 and name[i-1] == typed[j]:
                j += 1
            else:
                return False
        while j < len(typed):
            if name[i-1] != typed[j]:return False
            j += 1
         
        if i < len(name):return False
        
        return True