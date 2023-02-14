#Logic: String is palindrome 
# 2 Base cases 
# One outright rejection if the 1st element is not equal to the last element. 
# string str 
def isPalindrome(str,i):
    #str="abba"
    #print(str[len(str)-1])
    if str[i]!=str[len(str)-1]:
        return False 
    if (i >=len(str)/2):
        return True
    return isPalindrome(str,i+1)

str="abba"
print(isPalindrome(str,len(str)-1))

# str="abbac"
# print(isPalindrome(str,0,len(str)-1))
