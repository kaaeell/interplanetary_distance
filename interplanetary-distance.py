import math
import random

# storing old calcs here
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
            print("invalid input bro just numbers")


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

    # just picking planets here
    def pick(msg):
        while True:
            try:
                choice = int(input(msg))
                if choice in planets:
                    return planets[choice]
                else:
                    print("pick a valid number bro")
            except ValueError:
                print("numbers only pls")

    p1_name, p1 = pick("Choose planet 1: ")
    p2_name, p2 = pick("Choose planet 2: ")

    return p1_name, p1, p2_name, p2


def show_fun_fact():
    facts = [
        "Jupiter is so big it could fit all planets inside it 😳",
        "A day on Venus is longer than a year there",
        "Saturn could float in water (crazy but true)",
        "Mars sunsets are blue not red",
        "space is just silent no sound at all"
    ]
    print(f"\nfun fact: {random.choice(facts)}")


def main():
    print("Space Distance Calculator v5")
    print("yeah it does math in space or something\n")

    while True:
        mode = input("1 planets | 2 custom | 3 history: ").strip()

        # showing old stuff
        if mode == "3":
            if not history:
                print("nothing saved yet lol")
            else:
                print("\nhistory:")
                for item in history:
                    print(item)
            continue

        # custom coords mode
        if mode == "2":
            p1 = get_coordinates("Point 1")
            p2 = get_coordinates("Point 2")
            p1_name, p2_name = "Point 1", "Point 2"
        else:
            p1_name, p1, p2_name, p2 = choose_planets()

        distance = calculate_distance(p1, p2)

        # convert to km because raw numbers are useless
        distance_km = distance * 1_000_000

        result = f"{p1_name} ↔ {p2_name}: {distance:.2f} million km ({distance_km:.0f} km)"
        print("\nDistance:", result)

        history.append(result)

        # light speed calc because why not
        light_speed = 299_792
        time_seconds = distance_km / light_speed
        time_minutes = time_seconds / 60

        print(f"light travel time: {time_seconds:.2f} sec ({time_minutes:.2f} min)")

        # random reactions because it feels alive
        if distance > 1000:
            print("that's insanely far bro")
        elif distance > 300:
            print("kinda far ngl")
        else:
            print("pretty close actually")

        show_fun_fact()

        # loop control
        again = input("\nrun again? (y/n): ").lower()
        if again != "y":
            print("ok done")
            break


if __name__ == "__main__":
    main()
