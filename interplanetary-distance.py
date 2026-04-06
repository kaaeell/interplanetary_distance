import math

# Space Distance Calculator v3
# simple project, clean logic, a bit of fun

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def get_coordinates(name):
    while True:
        try:
            print(f"\nEnter coordinates for {name} (in million km)")
            x = float(input("x: "))
            y = float(input("y: "))
            return (x, y)
        except ValueError:
            print("invalid input, try again")


def choose_planets():
    planets = {
        1: ("Earth", (0, 0)),
        2: ("Mars", (225, 0)),
        3: ("Venus", (108, 0)),
        4: ("Jupiter", (778, 0)),
        5: ("Saturn", (1427, 0))
    }

    print("\nAvailable planets:")
    for num, (name, _) in planets.items():
        print(f"{num}. {name}")

    def pick(msg):
        while True:
            try:
                choice = int(input(msg))
                if choice in planets:
                    return planets[choice]
                else:
                    print("choose a valid number")
            except ValueError:
                print("numbers only pls")

    p1_name, p1 = pick("Choose planet 1: ")
    p2_name, p2 = pick("Choose planet 2: ")

    return p1_name, p1, p2_name, p2


def main():
    print("🌌 Space Distance Calculator v3")
    print("let's measure some space stuff\n")

    mode = input("1 = planets | 2 = custom coordinates: ").strip()

    if mode == "2":
        p1 = get_coordinates("Point 1")
        p2 = get_coordinates("Point 2")
        p1_name, p2_name = "Point 1", "Point 2"
    else:
        p1_name, p1, p2_name, p2 = choose_planets()

    distance = calculate_distance(p1, p2)

    print(f"\nDistance between {p1_name} and {p2_name}: {distance:.2f} million km")

    # small personality
    if distance > 1000:
        print("😱 that's insanely far")
    elif distance > 300:
        print("😳 long distance relationship level")
    elif distance > 100:
        print("🙂 decent space gap")
    else:
        print("🚀 pretty close actually")


if __name__ == "__main__":
    main()
