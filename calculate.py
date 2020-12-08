# from ctypes import *
import ctypes
from ctypes import *
import io



def calculation(expression):
    so_file = "static/tinyexpr.so"

    c_functions = CDLL(so_file)

    print(type(c_functions))
    expression = expression
    expression = expression.encode('latin-1')


    # run c function that prints to a file
    c_functions.evaluate(ctypes.c_char_p(expression))

    f = open("file.txt", "r", encoding='latin-1')
    results = f.read()
    # print(results)
    #results = results.split (",")
    results = results[:-1]
    # print(results)
    return results

