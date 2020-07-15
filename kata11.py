#Consecutive strings
#You are given an array strarr of strings and an integer k.
#Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example:
#longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

#n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

#Note
#consecutive strings : follow one after another without an interruption

#I'm defining a Python function to determine the longest string if the original strings are combined for every k consecutive strings.
#The function takes two parameters, strarr and k.

def longest_consec(strarr, k):
    n = len(strarr)
    if k > n or k <= 0:
        return ""
    y = list()
    for i in range(n):
        x="".join(strarr[i:i+k])
        y.append(x)

    return max(y,key=len)

print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"],2))

































