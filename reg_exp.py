import re
# Exercise 1 / Regular expression

txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match)  
span = match.span()
print(span)    
start, end = span
print(start, end)  
substring = txt[start:end]
print(substring)      