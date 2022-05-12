class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        lst = list(s)
        # print(lst)
        while part in "".join(lst):
            left = 0
            right = len(part)
            while right <= len(lst):
                string = lst[left:right]
                if "".join(string) == part:
                    print(left , right)
                    new_lst = []
                    for i in range(len(lst)):
                        if i not in range(left , right):
                            new_lst.append(lst[i])
                    print(new_lst)
                    lst = new_lst
                    break
                
                left += 1
                right += 1
            print(lst)
        return "".join(lst)
            
            
                
            
            
            
            
              
            
            