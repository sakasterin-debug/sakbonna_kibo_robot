import random 
battery = 100.0

for waypoint in range(1, 11):

    battery = battery - random.uniform(1.5, 3.5)
    print("Waypoint", waypoint, "- Battery:", round(battery, 1), "%")

    if battery < 75:
        print("Emergency Return Triggered!")
        break

    elif battery < 80:
        print("CAUTION: Battery is low!")