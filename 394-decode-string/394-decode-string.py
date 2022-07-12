class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "]":
                st = ""
                while stack[-1] != "[":
                    st = stack.pop() + st
        
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                print(k)
                stack.append(st * int(k))
            else:
                stack.append(i)
        return "".join(stack)