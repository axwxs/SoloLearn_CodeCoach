'''

Adding Words


You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

Sample Input
this
is
great

Sample Output
this-is-great

'''

def concatenate(*args, connect="-"):
	return connect.join(args)

# Another possibility
# def concatenate(*args):
# 	return "-".join(args)

    
print(concatenate("I", "love", "Python", "!"))
