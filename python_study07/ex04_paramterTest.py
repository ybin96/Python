from builtins import bool


def pro(a,b=None):
    print(a)
    if b != None:
        print(b)
    print("-"*50)

pro("hello", "python")