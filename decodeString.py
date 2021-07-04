# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:30:22 2021

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

@author: Norman
"""
def decodeString(s):
   stack = []
   curString = ""
   curK = 0
        
   for char in s:
       if char == "[":
           stack.append(curString)
           stack.append(curK)
           curString = ""
           curK = 0
       elif char == "]":
           prevK = stack.pop()
           prevString = stack.pop()
           curString = prevString + prevK*curString
       elif char.isdigit():
           curK = curK*10 + int(char)
       else:
           curString += char
                
   return curString

print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
print(decodeString("2[abc]3[cd]ef"))
