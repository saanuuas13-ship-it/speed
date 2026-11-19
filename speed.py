import sys

def calculate_speed(distance, time):
    if time > 0:
        return distance / time
    else:
        return "Invalid time"

distance = float(sys.argv[1])
time = float(sys.argv[2])

print("Speed:", calculate_speed(distance, time))