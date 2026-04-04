import math

# 🚀 Space Distance Calculator v3
# Now with more options and fun facts. Because space is big. Really big.

def calculate_distance(p1, p2):
    """Calculate distance between two points in 2D space."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def get_planet_position(name):
    """Ask user for planet coordinates in million km."""
    print(f"\nEnter coordinates for {name} (in million km):")
    
    while True:
        try:
            x = float(input("  x: "))
            y = float(input("  y: "))
            return (x, y)
        except ValueError:
            print("⚠️  Please enter a valid number. Space math doesn't forgive mistakes!")


def select_predefined_planets():
    """User can choose planets from a predefined list."""
    planets = {
        "Earth": (0, 0),
        "Mars": (225, 0),
        "Venus": (108, 0),
        "Jupiter": (778, 0),
        "Saturn": (1427, 0)
    }
    print("\n🌍 Available planets:")
    for i, planet in enumerate(planets.keys(), start=1):
        print(f"  {i}. {planet}")
    
    def choose_planet(prompt):
        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= len(planets):
                    return list(planets.values())[choice-1], list(planets.keys())[choice-1]
                else:
                    print("⚠️  Invalid number, try again.")
            except ValueError:
                print("⚠️  Enter a number, not a black hole.")

    p1_pos, p1_name = choose_planet("Choose Planet 1 by number: ")
    p2_pos, p2_name = choose_planet("Choose Planet 2 by number: ")
    return p1_pos, p2_pos, p1_name, p2_name


def main():
    print("🌌 Welcome to the Space Distance Calculator v3")
    print("Let's measure the cosmic gaps between your favorite planets 👀")

    choice = input("\nDo you want to use (1) predefined planets or (2) custom coordinates? (1/2): ").strip()

    if choice == '2':
        planet1 = get_planet_position("Planet 1")
        planet2 = get_planet_position("Planet 2")
        p1_name = "Planet 1"
        p2_name = "Planet 2"
    else:
        planet1, planet2, p1_name, p2_name = select_predefined_planets()

    distance = calculate_distance(planet1, planet2)

    print("\n🌠 Calculating distance...")
    print(f"📏 Distance between {p1_name} and {p2_name}: {distance:.2f} million km")

    # Fun comments based on distance
    if distance > 1000:
        print("😱 Whoa! That's basically light-years away (almost).")
    elif distance > 300:
        print("😳 That's FAR... like long-distance relationship far.")
    elif distance > 100:
        print("🙂 Not too close, not too far. Space vibes.")
    else:
        print("🚀 Pretty close! Elon would approve.")

    # Optional: give a fun fact about distance
    if distance < 1:
        print("✨ Wow, practically neighbors! Time for interplanetary coffee? ☕")
    elif distance < 50:
        print("🪐 You could almost throw a meteor and hit it. Not recommended though.")


if __name__ == "__main__":
    main()
