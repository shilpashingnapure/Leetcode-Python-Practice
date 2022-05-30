class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ans = "Neither"
        if "." in queryIP:
            check = self.check_For_IP4(queryIP)
            if check:
                ans = "IPv4"
        else:
            check = self.check_For_IP6(queryIP)
            if check:
                ans = "IPv6"
        return ans
    
    def check_For_IP4(self , ip):
        ip = ip.split('.')
        
        
        if len(ip) != 4:
            return False
        
        #check valid
        for i in ip:
            if i.isnumeric():
                a = int(i)
                if a < 0 or a > 255 or (i[0] == "0" and len(i) > 1):
                    return False
            elif i.isnumeric() == False:
                return False
        return True
    
    def check_For_IP6(self , ip):
        ip = ip.split(":")
        print(ip)
        if len(ip) != 8:
            return False
        for i in ip:
            if len(i) > 4 or len(i) < 1:
                return False
            flag = ""
            for j in i:
                if j.isupper() or j.islower():
                    j = j.lower()
                    if ord(j) > ord("f") or ord(j) < ord("a"):
                        return False
        return True       