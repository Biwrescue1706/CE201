INCHES_PER_FT = 12
feet = "plural of foot"

def get_feet(ht_in_inches):
    feet = ht_in_inches //INCHES_PER_FT
    return feet
total = get_feet(68)
print (total)
print (INCHES_PER_FT)

def get_feet(ht_in_inches):
    feet = ht_in_inches //INCHES_PER_FT
    return feet
get_feet(68)
print (feet)
#กลับค่า
def swap (a,b):
    tmp = a
    a = b
    b = tmp
total1 = swap(1,2)

def foo(a,b):
    x=a
    y=b
    return x*y+y
x=2
foo (3,4)
print (x)