def print_hello(msg):
    print(msg)

def print_hello_args(*args):
    print(args)
    for arg in args:
        print(arg)

def print_hello_kwargs(**kwargs):
    print(kwargs)

print_hello('hello')
print_hello_args('hello')
print_hello_args('hello', 'everyone', 'here')
print_hello_kwargs(msg1='hello', firstname='gael')

a = {'hello': 'hello'}
print(a)

str = 'hello'
str2 = 'y' + str[1:]
print(str2)
