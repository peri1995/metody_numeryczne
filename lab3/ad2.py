from math import *


def countField(figura=None, *args):
    if len(args) > 2:
        raise ()
    for i in args:
        if i < 0:
            raise ()
    if figura == 'circle' and len(args) < 2:
        print(f'Circle field: {pi * (args[0] ** 2)}')
        return (pi * (args[0] ** 2))

    elif figura == 'rectangle':
        print(f'Rectangle field: {args[0] * args[1]}')
        return (args[0] * args[1])
    elif figura == 'triangle':
        print(f'Triangle field: {(args[0] * args[1]) / 2}')
        return ((args[0] * args[1]) / 2)
    elif figura == 'rhombus':
        print(f'Rhombus field: {(args[0] * args[1]) / 2}')
        return ((args[0] * args[1]) / 2)
    else:
        raise ()


def compare(*args):
    par1, par2 = args

    if len(par1) == 3:
        a, b = par1[1:]
        wynik1 = countField(par1[0], int(a), int(b))
    else:
        a = par1[1]
        wynik1 = countField(par1[0], int(a))
    if len(par1) == 2:
        a, b = par2[1:]
        wynik2 = countField(par2[0], int(a), int(b))
    else:
        a = par2[1]
        wynik2 = countField(par2[0], int(a))
    if wynik1 > wynik2:
        print('The first one is bigger')
    else:
        print('The second one is bigger')


try:
    compare(['circle', 2], ['triangle', 20, 4])
except TypeError:
    print('Zle dane')