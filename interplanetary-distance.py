import math
#We’ll calculate the distance between two planets using coordinates.
# Planet positions in millions of km (simplified 2D)
earth_pos = (0,0)   # Earth at origin
mars_pos = (225,0)  # Mars ~225 million km away on x-axis

d = math.sqrt((mars_pos[0] - earth_pos[0])**2 + (mars_pos[1] - earth_pos[1])**2)

# Calculate distance
print("🌌 Distance between Earth and Mars:")
print(f"{d} million km")