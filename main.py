def main():
    foo(5, b=4)
    count(1,2,3,4,5)
    func(a=3, b=5, function=lambda a, b: a * b)
    return

def foo(a, /, *, b):
    print(a+b)
    return

def count(*numbers):
    for x in numbers:
        print(x)
    return

def func(*, a, b, function):
    print(function(a,b))
    return

main()