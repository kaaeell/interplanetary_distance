import math

# 🚀 Space Distance Calculator v2
# Because manually calculating space distances is... not it.

def calculate_distance(p1, p2):
    """Calculate distance between two points in 2D space."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def get_planet_position(name):
    """Ask user for planet coordinates."""
    print(f"\nEnter coordinates for {name} (in million km):")
    
    x = float(input("  x: "))
    y = float(input("  y: "))
    
    return (x, y)


def main():
    print("🌌 Welcome to the Space Distance Calculator")
    print("Let's see how far your planets are 👀")

    # Default planets (because Earth deserves to be default)
    earth_pos = (0, 0)

    choice = input("\nDo you want to use custom planets? (y/n): ").lower()

    if choice == 'y':
        planet1 = get_planet_position("Planet 1")
        planet2 = get_planet_position("Planet 2")
    else:
        # Classic Earth → Mars setup
        planet1 = earth_pos
        planet2 = (225, 0)  # Mars-ish

    distance = calculate_distance(planet1, planet2)

    print("\n🌠 Calculating distance...")
    print(f"📏 Distance: {distance:.2f} million km")

    # Just a little personality 😏
    if distance > 300:
        print("😳 That's FAR... like long-distance relationship far.")
    elif distance > 100:
        print("🙂 Not too close, not too far. Space vibes.")
    else:
        print("🚀 Pretty close! Elon would approve.")


if __name__ == "__main__":
    main()
