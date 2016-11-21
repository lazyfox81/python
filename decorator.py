#!/usr/bin/python
def decorator(func):
    def wrapper():
        print ("Bla, bla, Bla")
        return func()
    return wrapper

@decorator
def say():
    print("Hello")

# decorator(say)()
say()

