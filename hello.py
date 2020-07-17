# clear terminal screen
import os
os.system('clear')

name = "Rafael"
sports = ['tennis', 'soccer', 'darts', 'cards']

fav_pizza = {
    "Raf": "Pepperoni",
    "Bob": "Mushroom",
    "Mary": "Cheese"
}

for a in range(4):
    # print compliment to the screen
    print(name + " plays " + sports[a])

print("\n", sports[3])

print("\n", fav_pizza["Raf"])
