while True:
    line = input('> ')
    if line[0] == '#':
        print('# is a symbol')
        continue
    elif line == 'done':
        break
    else:
        print('what do you mean? # or done!')
print("\n" + "see you later")
