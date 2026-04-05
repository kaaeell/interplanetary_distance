import math

# Space Distance Calculator v4
# yeah... we measure space now 😎

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def get_coordinates(name):
    print(f"\nEnter coordinates for {name} (million km):")

    while True:
        try:
            x = float(input("  x: "))
            y = float(input("  y: "))
            return (x, y)
        except:
            print("bro... numbers only 💀")


def choose_planets():
    planets = {
        "Earth": (0, 0),
        "Mars": (225, 0),
        "Venus": (108, 0),
        "Jupiter": (778, 0),
        "Saturn": (1427, 0)
    }

    print("\nAvailable planets:")
    for i, name in enumerate(planets, start=1):
        print(f"{i}. {name}")

    names = list(planets.keys())
    values = list(planets.values())

    def pick(msg):
        while True:
            try:
                choice = int(input(msg))
                if 1 <= choice <= len(names):
                    return names[choice-1], values[choice-1]
                else:
                    print("not on the list bro 😭")
            except:
                print("type a number... not a spell")

    name1, p1 = pick("Planet 1: ")
    name2, p2 = pick("Planet 2: ")

    if name1 == name2:
        print("you really picked the same planet twice 💀 try again")
        return None

    return name1, p1, name2, p2


def show_fun_comment(distance):
    if distance > 1000:
        print("😱 that's crazy far... even light needs a break")
    elif distance > 300:
        print("😳 long distance relationship level")
    elif distance > 100:
        print("🙂 chill distance, nothing dramatic")
    else:
        print("🚀 kinda close ngl")

    if distance < 1:
        print("✨ basically neighbors, go say hi")
    elif distance < 50:
        print("🪐 you could almost throw a rock (please don't)")


def main():
    print("\n🌌 Space Distance Calculator v4")
    print("we measure space so you don't have to")

    choice = input("\n1 = planets | 2 = custom coords → ")

    if choice == "2":
        p1 = get_coordinates("Planet 1")
        p2 = get_coordinates("Planet 2")
        name1, name2 = "Planet 1", "Planet 2"
    else:
        result = choose_planets()
        if result is None:
            return
        name1, p1, name2, p2 = result

    distance = calculate_distance(p1, p2)
    distance_km = distance * 1_000_000

    print("\ncalculating...")
    print(f"\n📏 {name1} ↔ {name2}")
    print(f"{distance:.2f} million km")
    print(f"{distance_km:,.0f} km")

    show_fun_comment(distance)

    print("\n(note: this is simplified 2D space, NASA please don't sue me 😂)")


# loop so user doesn't have to restart every time
while True:
    main()
    again = input("\nagain? (y/n): ").lower()
    if again != "y":
        print("👋 leaving the universe... bye")
        break
