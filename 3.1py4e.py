hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h > 40:
    extraHours = h - 40
    pay = (40 * 10.50) + (extraHours * 1.5 * 10.50)
    print(str(pay))
else:
    pay = (40 * 10.50)
    print(str(pay))
    
print("done!!")
