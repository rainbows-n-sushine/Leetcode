class Solution:
    def clearDigits(self, s:str)->str:
        res=[]
        delete_count=0

        def isDigit(c):
            return ord("0") <= ord(c) <=ord("9")
        
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                delete_count+=1
            elif delete_count:
                delete_count-=1
            else:
                res.append(s[i])

        return "".join(res[::-1])

solution=Solution()
input_string="abdy453"
result=solution.clearDigits(input_string)
print(result)

          