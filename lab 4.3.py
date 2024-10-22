def palindrome(text):
    a = text[::1]
    b = text[::-1]
    return a==b
print (palindrome('noon'))
print (palindrome('computer'))
print (palindrome('car'))
print (palindrome('racecar'))