compliment = "hello mate!"

try:
    x = int(compliment)
except:
    x = -1

print('print1:', x)

try:
    x = x + 1
except:
    x = -1

print('print2:', x)
