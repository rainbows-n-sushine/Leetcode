# first take a string input(Assuming that thestring is written in a such a way that characters come first before digits and the preceeding digits are always less or equal to the number of characters after)
#loop through the reversed string
# check if the current character is a digit, if so skip appending character and increase delete_count by adding 1 to it.
# check if it is a character
# if it is a character, check if delete_count is 0, if it is then append the character to empty list res
# if it is a character,and delete_count was greater than zero, update delete_count subtracting 1 and skip appending to res-list

class Solution:
    def clearDigits(self, s:str)->str:
        res=[]
        for i in range(len(s)):
            if s[i].isdigit():
                res.pop()
            else:
                res.append(s[i])
        return "".join(res)

solution= Solution()
input_str="abcdfs6535"
result=solution.clearDigits(input_str)
print(result)