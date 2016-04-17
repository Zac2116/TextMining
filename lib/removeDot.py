'''
import re
def removeDot(s):
	if s[0] == '.':
		s = s[1:]
	if s[len(s)-1] == '.':
		s = s[:-1]
	return s
'''
def removeDot(s):
        num = ["0","1","2","3","4","5","6","7","8","9"]
        if s[0] == ".":
                s = removeDot(s[1:])
        elif s[len(s)-1]==".":
                s = removeDot(s[:-1])
        else:
                for i in range(1,len(s)-1):
                        if s[i]=="." and (s[i-1] not in num or s[i+1] not in num):
                                s = removeDot(s[:i]+s[i+1:])
                                break
        return s
