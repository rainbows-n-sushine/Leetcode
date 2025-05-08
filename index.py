# first take a string input(Assuming that thestring is written in a such a way that characters come before digits and the preceeding characters are always greater or equal to the number of digits after)
#loop through the reversed string
# check if the current character is a digit, if so skip appending character and increase delete_count by adding 1 to it.
# check if it is a character
# if it is a character, check if delete_count is 0, if it is then append the character to empty list res
# if it is a character,and delete_count was greater than zero, update delete_count subtracting 1 and skip appending to res-list

class Solution:
    def clearDigits(self, s:str)->str:
        res=[]
        delete_count=0
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                delete_count+=1
            elif delete_count:
                delete_count-=1
            else:
                res.append(s[i])
        return "".join(res[::-1])
    
solution=Solution()
input_str="abcdsh665"
result=solution.clearDigits(input_str)
print(result)

     
