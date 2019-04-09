from math import *

def countField(figura=None, *args):
    if len(args) > 2:
        raise()
    for i in args:
        if i < 0:
            raise()
    if figura == 'circle' and len(args) < 2:
        print(f'Circle field: {pi * (args[0]**2)}')
    elif figura == 'rectangle':
        print(f'Rectangle field: {args[0]*args[1]}')
    elif figura == 'triangle':
        print(f'Triangle field: {(args[0]*args[1])/2}')
    elif figura == 'rhombus':
        print(f'Rhombus field: {(args[0]*args[1])/2}')
    else:
        raise()

try:
    countField('circle', 2)
except TypeError:
    print('Zle dane')

