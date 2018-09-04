def switch_func(value, x,y):
    return {
        'a': lambda x: x+y,
        'b': lambda x: x*y,
        'c': lambda x: x-y,
        'd': lambda x: x/y
    }.get(value)(x)

# take user input
inp = input('Input a operation Character : ')

print('The result is : ', switch_func(inp, 4, 2))












#area = lambda radius : 3.14*radius*2
#print("area of the circle:")
#print(area(4))
#areat = lambda h,b : h*b
#print("area of the triangle:")
#print(areat(2,3))
#areas = lambda a : a*a
#print("area of the square:")
#print(areas(9))
