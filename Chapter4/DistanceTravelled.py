time = int(input("How long were you travelling (hours): "))
speed = int(input("What was your speed (km/h): "))
loop = 0

while loop < time:
    loop += 1
    distance = loop * speed
    print("In hour", loop, "you travelled", distance, "km")
