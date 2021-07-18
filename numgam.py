n = int(input('enter an integer: '))
print( 'is', n, '"greater" than, "less" than, or "equal" to 14?' )
m = input('answer: ')

greater = m
x = 'greater'
y = 'less'
z = 'equal'

if n > 14 and m is x:
    print( 'Correcto-mante! 1,000 points for you!' )
elif n < 14 and m is x:
    print( 'oh noze bros, negative 1,000 points for you!!' )
elif n is 14 and m is x: 
    print( 'wrong wrong wrong! negative 1,000 points for you!!' )
elif n > 14 and m is y:
    print( 'oh noze bros, negative 1,000 points for you!!' )
elif n < 14 and m is y:
    print( 'Correcto-mante! 1,000 points for you!' )
elif n is 14 and m is y:
    print( 'wrong wrong wrong! negative 1,000 points for you!!' )
elif n > 14 and m is z:
    print( 'oh noze bros, negative 1,000 points for you!!' )
elif n < 14 and m is z:
    print( 'wrong wrong wrong! negative 1,000 points for you!!' )
elif n is 14 and m is z:
    print( 'Correcto-mante! 1,000 points for you!')

elif n is 14 or n>14 or n<14 and m is not ('greater' or 'less' or 'equal'):
    print('answer the question! or use the words in quotes, tyvm' )

#if n < 14:
    #if m is greater:
            #print( 'oh noze bros, negative 1,000 points for you!!' )
    #if m is less:
            #print( 'Correcto-mante! 1,000 points for you!' )
    #if m is equal: 
            #print( 'wrong wrong wrong! negative 1,000 points for you!!')
    #if m is not (greater or less or equal):
            #print('answer the damn question! or use the words in quotes, tyvm')
#if n is 14:
    #if m is greater:
            #print( 'oh noze bros, negative 1,000 points for you!!' )
    #if m is less:
            #print( 'wrong wrong wrong! negative 1,000 points for you!!' )
    #if m is equal: 
            #print( 'Correcto-mante! 1,000 points for you!')
    #if m is not (greater or less or equal):
            #print('answer the damn question! or use the words in quotes, tyvm')
