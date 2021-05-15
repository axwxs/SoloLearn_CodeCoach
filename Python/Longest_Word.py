'''
Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome

'''

txt = input()

def findlongestword(txt):
    longestword = ''
    for word in txt.split():
        if len(word) > len(longestword):
            longestword = word
    print(longestword)
    
findlongestword(txt)
