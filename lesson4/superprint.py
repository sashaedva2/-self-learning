def print_them_all_v4(a, b=5, *args, **kwargs):
    print('print_them_all_v4')
    print('a и b:', a, b)
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v4(5, 6, 7, 8, cat='мяу!')
print_them_all_v4(5, b=8, cat='мяу!')
print_them_all_v4(5, cat='мяу!', address='Moscow')
