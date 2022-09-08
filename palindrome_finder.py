import re

def palindrome(phrase):
    forward = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backward = forward[::-1]
    return forward == backward

print(palindrome('ssass'))