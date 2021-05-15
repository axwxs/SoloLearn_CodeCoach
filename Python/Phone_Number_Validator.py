'''
You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9. 
Output "Valid" if the number is valid and "Invalid", if it is not. 

Sample Input
81239870

Sample Output 
Valid
'''

import re
#your code goes here

x = input()

pattern = r"^(9|8|1)+(\d+\d+\d+\d+\d+\d+\d)$"

match = re.match(pattern, x)


if match:
	if(len(x)) == 8:
		print('Valid')
	else:
		print('Invalid')
else:
	print('Invalid')
