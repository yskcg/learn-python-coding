# -*- coding: utf-8 -*-
import functools

def log(text):
    if isinstance(text,(str,int,float)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print("begin call ")
                print("%s,%s():" %(text ,func.__name__))
                func(*args,**kw)
                print("end call")
            return wrapper
        return decorator
    else:
        func = text
        def wrapper(*args,**kw):
                print("begin call ")
                print("%s():" %func.__name__)
                func(*args,**kw)
                print("end call")
        return wrapper

@log("execute")
def hello_python():
    print("i love python")

hello_python()

@log
def hello_c():
    print("I love c")

hello_c()
