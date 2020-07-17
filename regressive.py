import time

regressive = 10
while regressive > 0:
    print(regressive)
    regressive = regressive - 1
    time.sleep(1)
    if regressive == 0:
        print("LAUNCH!")
