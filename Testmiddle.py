
def middle (text):
    size = len(text)
    start2 = size//3
    start3 = (2*size)//3
    middle_third = text[start2:start3]
    return middle_third
middle_third1=middle("xxxxyyyyzzzz")
print (middle_third1)