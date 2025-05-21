import re

string ="hello"
pattern ="h"
result = re.match(pattern,string)
print(result)   


string ="hello"
pattern ="llo"
result = re.search(pattern,string)
print(result)

string ="hello"
pattern ="l"
re.findall(pattern,string)
#meta characters
# . - any character except newline
# ^ - starts with
# $ - ends with
# * - zero or more occurrences
# + - one or more occurrences
# ? - zero or one occurrences
# {} - exactly the specified number of occurrences
# [] - a set of characters
# | - either or

# * - zero or more occurrences
import re
string ="abc"
pattern =r"ab*c"
result = re.match(pattern,string)
print(result)   
string ="ac"
pattern =r"ab*c"
result = re.match(pattern,string)
print(result)   
string ="abbbbbbbc"
pattern =r"ab*c"
result = re.match(pattern,string)
print(result)   

# + - one or more occurrences
import re
string ="abc"
pattern =r"ab+c"
result = re.match(pattern,string)
print(result)   
string ="ac"
pattern =r"ab+c"
result = re.match(pattern,string)
print(result)   
string ="abbbbbbbc"
pattern =r"ab+c"
result = re.match(pattern,string)
print(result)   

