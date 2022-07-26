class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        for i in range(len(s2)):
            if s2[i] in d:
                d[s2[i]] -= 1
            if i >= len(s1) and s2[i-len(s1)] in d:
                d[s2[i-len(s1)]] += 1
            print(d)
            if all([d[i] == 0 for i in d]):
                return True
        return False
#         if len(s1) > len(s2):return False
#         d = Counter(s1)
        
#         left = 0
#         right = len(s1)
#         while right <= len(s2):
#             if self.match(left , right , s2 , d):
#                 return True
#             else:
#                 left += 1
#                 right += 1
#         return False

        
#     def match(self , left , right , s2 , d):
#         d1 = {}
#         for i in range(left , right):
#             if s2[i] in d1:
#                 d1[s2[i]] += 1
#             else:
#                 d1[s2[i]] = 1
        
#         return d == d1
            
    
            