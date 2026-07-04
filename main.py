def main():
    foo(5, b=4)
    count(1,2,3,4,5)
    func(a=3, b=5, function=lambda a, b: a * b) #oh dude i love lambda funcitons
    return

def foo(a, /, *, b): #these things are cool
    print(a+b)
    return

def count(*numbers):    #as this is cool too, i learned i could do **var
    for x in numbers:   #to make them dictionaries instead of tupples but its too early for that
        print(x)
    return

def func(*, a, b, function):
    print(function(a,b))
    return

main()