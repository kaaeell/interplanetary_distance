import math
import random

# Space Distance Calculator v4
# still simple, just got a bit smarter

history = []


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


def show_fun_fact():
    facts = [
        "Jupiter is so big it could fit all planets inside it 😳",
        "A day on Venus is longer than a year there",
        "Saturn could float in water (if you find a big enough ocean lol)",
        "Mars sunsets are blue, not red",
        "Space is completely silent, no sound at all"
    ]
    print(f"\n🧠 fun fact: {random.choice(facts)}")


def main():
    print("🌌 Space Distance Calculator v4")
    print("now with memory and random space knowledge\n")

    while True:
        mode = input("1 = planets | 2 = custom coordinates | 3 = history: ").strip()

        if mode == "3":
            if not history:
                print("\nno history yet, go calculate something first")
            else:
                print("\n📜 previous calculations:")
                for item in history:
                    print(item)
            continue

        if mode == "2":
            p1 = get_coordinates("Point 1")
            p2 = get_coordinates("Point 2")
            p1_name, p2_name = "Point 1", "Point 2"
        else:
            p1_name, p1, p2_name, p2 = choose_planets()

        distance = calculate_distance(p1, p2)

        # convert to km
        distance_km = distance * 1_000_000

        result = f"{p1_name} ↔ {p2_name}: {distance:.2f} million km ({distance_km:.0f} km)"
        print(f"\nDistance: {result}")

        history.append(result)

        # personality stays
        if distance > 1000:
            print("😱 that's insanely far")
        elif distance > 300:
            print("😳 long distance relationship level")
        elif distance > 100:
            print("🙂 decent space gap")
        else:
            print("🚀 pretty close actually")

        show_fun_fact()

        again = input("\nrun again? (y/n): ").lower()
        if again != "y":
            print("alright, back to earth 🌍")
            break


if __name__ == "__main__":
    main()
