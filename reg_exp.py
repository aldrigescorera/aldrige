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



'''re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string'''