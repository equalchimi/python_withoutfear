# next line is so sys command works. comes as part of python package
import sys

# page 9
print(5)
print(10+15)
# next line is to see what version of python you are on!
print(sys.version)
print()


# page 10
print(2 ** 5)
print()

# page 11
print( 10 ** 40 == 10 ** 40 + 1e-100000 )
print()

# page 13
print( 5 * 2 ** 5 )
# ^ so exponents take a higher precedence than multiplication
print( (10 ** 100 +1) % 13 )
# we get remainder 4, so we need 9 more numbers to get a whole 13, and therefore make remainder 0, so add 9 to that 1!
print( (10 ** 100 +10) % 13 )
print()

# on my own for a bit...
x = 5
y = 2
print( x + y )
print( 'is x greater than 3 if x is 5?' )
if x > 3:
    print( 'yes,', x, 'is greater than', 3 )
if x <= 3:
    print( 'no,', x, 'is not greater than', 3 )
x = 5
print()

# page 16
print('is 5/2 equal to 10/4')
print(5/2 == 10/4)
print('is 5.04/2 equal to 10/4')
print(5.04/2 == 10/4)
print('is 5.000000000000000004/2 equal to 10/4')
print(5.000000000000000004/2 == 10/4)
print()

# page 17
e = 6
g = 5
k = 7
# variables on right of = sign must be predefined or error will occur
#e = f
#print(f)
#>>> error, 'f' not defined

# page 18
# the same variable can appear on both sides of the = sign, the old on used in calc.
B = 5
B = B + 1
print('B = 5')
print('B = B + 1')
print(B)
print()

# page 20
# quadratic formula! more manual
print('quadratic formula:')
a = 1
b = -1
c = -1
determ = (b**2 - 4 * a * c) ** .5
print(determ)
x = ((-b + determ) / 2 * a)
print(x)
print()

# page 23
# naming conventions
print('naming conventions')
s1 = 'Lion\'s World'
print(s1) #strings will be learned later!
print(type(s1))
print('~~~~~~~~')
wee_list = ['Lee', 'Pika', 'Pachi']
print(wee_list)
print(type(wee_list))
print('~~~~~~~~')
y = 0.578
print('y = 0.578')
print(type(y))
print('~~~~~~~~')
m = 235
print('m = 235')
print(type(m))
print()

# page 24
# tuple assignment!
print('tuple assignment:')
i, j, k = -32, 54, 734
print('i, j, k = -32, 54, 734')
print(i)
print(j)
print(k)
print()

# another shortcut
a = 5
b = 9
print('a = 5')
print('b = 9')
print('the sum of a and b is:')
print(a + b)
a, b = a + b, a
print('a, b = a + b, a')
print('now a is equal to:')
print(a)
print('now b is equal to:')
print(b)
print('...the old value of a, and a is the sum of their old values!')
print()

# page 25
L = 6   ;print('L = 6')
L += 7  ;print('L += 7')
print('L = ')  ;print(L)
# so that += essentially means that you take the initial value of the variable, and perform the operation right before the = with the value after the =
print('so that += essentially means that you take the initial value of the variable, and perform the operation right before the = with the value after the =')
print()
# ***variable must already be defined, and += etc cannot be used in larger expressions


## end chapter 2

