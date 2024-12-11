def alphabet(a, b, *args, other_letter, **kwargs):
    print('a -', a)
    print('b -', b)
    for key in args:
        print('args -', key)
    print('other_letter -', other_letter)
    for key in kwargs:
        print(key, '-', kwargs[key])

alphabet(1, 2, 4, 5, 6, c=3, g=7, h=8, other_letter=9)