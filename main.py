#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING expression as parameter.
#

openParenthesis=["(", "{", "["]
closeParenthesis=[")", "}", "]"]

def isBalanced(expression):
    stack=[]
    
    for i in expression:
        if i in openParenthesis:   
            stack.append(i)
        elif i in closeParenthesis:
            position=closeParenthesis.index(i)
            if ((len(stack)>0) and (openParenthesis[position]==stack[len(stack)-1])):  #if stack is not empty and the top element in the stack is the matching open parenthesis for the current closed parenthesis in the loop
                stack.pop()
            else:
                return "NO"  
                
    if len(stack)==0:
        return "YES"  
    else:
        return "NO"                

string = "{[]{()}}"
print(string,"-", isBalanced(string))
 
string = "[{}{})(]"
print(string,"-", isBalanced(string))
 
string = "((()"
print(string,"-",isBalanced(string))