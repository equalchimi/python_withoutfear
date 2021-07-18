# page 30
## defining functions

print('defining functions: cels to fahr')

def convert(cels) :                 # def = define, handy, right? convert is just what we named our 'function command'
    fahr = cels * 1.8 + 32.0        # the calculation!
    return fahr                     # what you want to get back from using the function, the output

print('convert(22)')
print(convert(22))
print()

# page 32
## another example

print('another example:')

def cm2in(x) :                      # converting centimeters to inches, so x would be in cm
    return x / 2.54                 # notice how this is only 2 lines

print('cm2in(195)')
print(cm2in(195))
print()

## Note! Consistently use either 4 spaces or a tab

# page 36
## adding text to our functions

print('adding text to the previous function:')

def cm2inII(x) :
    inches = x / 2.54
    print(x, 'cm =', inches, 'in')  # if you hadn't noticed already, extra spaces added b/w items sep. by commas

print('cm2inII(195)')
print(cm2inII(195))
print()

# page 38
## quadratic formula function!

print('turning quadratic formula into a function:')

def quad(a ,b, c) :
    determ = ((b**2 - 4*a*c)**0.5)
    x1 = (-b + determ) / 2*a
    x2 = (-b - determ) / 2*a
    print('x1 =', x1)
    print('x2 =', x2)

print('quad(2, 6, -8)')
print(quad(2, 6, -8))
print()

# page 40

print('testing plus/minus sign:')

def test(i, j) :                    # i am testing use of a plus/minus sign
    t = i +- j
    print(t)

print('test(5, 6)')
print(test(5, 6))                   # - sign takes precedence
print()

# page 41
## string input!

print('string input game:')

def deathnote() :
    print('>>welcome to Death Note!')
    name1_str = input('>>>Enter your full name: ')
    name2_str = input('>>>Enter their first name: ')
    name3_str = input('>>>Enter their last name: ')
    print('>>Here is the owner of this Death Note:', name1_str)
    print('>>Here is your first victim:', name2_str, name3_str)

print('deathnote()')
#print(deathnote())
print()

# page 42
## string input type

print('[testing input type]')

#def testII() :
    #testII_str = input('Age: ')     # asked to input a number, but stored as text, not a value
    #print('Next year you\'ll be', testII_str + 1)

#print('testII()')
#print(testII())                     # should get an error
print()

# page 43
## numeric input

print('numeric input: ')

def numput() :
    n = int(input('Enter an integer: '))    # notice the 'int'
    print('Thrice of that is', 3 * n)

print('numput()')
#print(numput())
print()

# page 44
## user friendly quadratic formula function using 'float'

print('user friendly quadratic formula function using \'float\'')

def quadII() :
    a = float(input('Enter a value: '))     #float can handle int, too
    b = float(input('Enter b value: '))
    c = float(input('Enter c value: '))
    determ = (b**2 - 4*a*c)**0.5
    x1 = (-b + determ) / (2*a)
    x2 = (-b - determ) / (2*a)
    print('x1 =', x1, 'x2 =', x2)

print('quadII()')
#print(quadII())
print()

## testing int with above function

print('testing int with above function')

def quadIII() :
    a = int(input('Enter a value: '))     # yes, float handles int but not vice versa
    b = int(input('Enter b value: '))
    c = int(input('Enter c value: '))
    determ = (b**2 - 4*a*c)**0.5
    x1 = (-b + determ) / (2*a)
    x2 = (-b - determ) / (2*a)
    print('x1 =', x1, 'x2 =', x2)

print('quadIII()')
#print(quadIII())
print()

print('testing!')
print(5*5-8*7/1)