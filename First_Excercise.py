import numpy as np
import matplotlib as mpl

def myfun(x):
    y = (x**2)+((x-2)**3)-5
    return y

def mybisection(a,b,e,iterm):
    # a,b endpoints, e tolerance
    c = (a + b) / 2.0
    i = 1
    while (b - a) / 2.0 > e and i <= iterm:
        if myfun(c) == 0:
            # return c
            print("number of iterations " + i + " bisection " + c)
        elif myfun(a) * myfun(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2.0
        i += 1
    # return c
    print("number of iterations "+i+" bisection "+c)

