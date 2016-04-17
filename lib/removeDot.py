import re
def removeDot(s):
	if s[0] == '.':
		s = s[1:]
	if s[len(s)-1] == '.':
		s = s[:-1]
	return s
