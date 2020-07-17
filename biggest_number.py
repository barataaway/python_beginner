largest = 0

print('The largest number is currently:', largest)

while True:
    a = input('> ')
    if a.isdigit():
        if int(a) > largest:
            largest = int(a)
            print('The largest number is now:', largest)
        else:
            print('The largest number is still:', largest)
    elif a == '#':
        print('ok, bye')
        break
    else:
        print('You\'ve got to type a integer or # to exit')
