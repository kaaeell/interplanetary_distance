"""
🚀 SPACE ADVENTURE - The Friendly Edition v3.5
A cozy space game where you explore, trade, and become a legend!
New: Space pets, random jokes, daily luck, and more!
"""

import math, random, time, json, os
from datetime import datetime

# ============================================
# YOUR SHIP - Your home in the stars
# ============================================
you = {
    "fuel": 5000,        # Gas to fly!
    "credits": 1000,     # Space money
    "missions": 0,       # How many trips
    "streak": 0,         # Hot streak!
    "morale": 80,        # Happy crew?
    "research": 0,       # Science points
    "rank": 1,           # Bounty hunter rank
    "record": 0,         # Furthest trip
    "trophies": [],      # Achievements
    "stuff": [],         # Your treasures
    "pets": [],          # NEW: Space pets!
    "luck": 0,           # NEW: Daily luck
    "last_play": None    # NEW: Track last play date
}

# ============================================
# YOUR CREW - Your space family
# ============================================
crew = [
    {"name": "Captain Rex", "skill": "Leadership", "level": 1, "xp": 0},
    {"name": "Engineer Jen", "skill": "Mechanics", "level": 1, "xp": 0},
    {"name": "Navigator Zoe", "skill": "Astrogation", "level": 1, "xp": 0},
    {"name": "Scientist Kim", "skill": "Research", "level": 1, "xp": 0},
    {"name": "Gunner Mack", "skill": "Combat", "level": 1, "xp": 0}
]

# ============================================
# THE COSMOS - All the cool stuff
# ============================================

# NEW: Space pets you can find!
space_pets = [
    "🐶 Space Dog", "🐱 Robot Cat", "🐹 Alien Hamster", 
    "🐉 Tiny Dragon", "🦊 Quantum Fox", "🐧 Space Penguin",
    "🦄 Nebula Unicorn", "🐙 Star Octopus"
]

# NEW: Funny space jokes!
jokes = [
    "Why did the star go to school? To get a little brighter!",
    "What do astronauts use to keep their pants up? An asteroid belt!",
    "Why don't aliens visit our solar system? They read the reviews... only one star!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key? The space bar!",
    "Why did the alien cross the galaxy? To get to the other side!",
    "What do you call a lazy astronaut? A space cadet!",
    "Why is space so clean? Because nobody dusts!"
]

# Planets you can visit
PLANETS = {
    1: ("Earth", (0,0)), 2: ("Mars", (225,0)), 3: ("Venus", (108,0)),
    4: ("Jupiter", (778,0)), 5: ("Saturn", (1427,0)), 6: ("Uranus", (2871,0)),
    7: ("Neptune", (4495,0)), 8: ("Mercury", (58,0)), 9: ("Pluto", (5906,0))
}

# Bad guys to catch
bounties = [
    {"name": "Red Pirate", "reward": 500, "level": 1, "hp": 3},
    {"name": "Shadow Corsair", "reward": 1000, "level": 2, "hp": 5},
    {"name": "Void Reaver", "reward": 2000, "level": 3, "hp": 7}
]

# Tech to unlock
tech = {
    "Fuel Efficiency": {"cost": 100, "owned": False},
    "Warp Drive": {"cost": 200, "owned": False},
    "Shield Tech": {"cost": 150, "owned": False}
}

# Achievements to earn
trophies = {
    "first": "🌱 Your first space trip!",
    "explorer": "🌌 You traveled far!",
    "fuel": "⛽ You found fuel in a nebula!",
    "rich": "💰 You're a space millionaire!",
    "legend": "⭐ You're a space legend!",
    "streak": "🔥 You're on fire!",
    "bounty": "💰 You caught a criminal!",
    "research": "🧠 You're a genius!",
    "pet": "🐾 You found a space pet!",
    "lucky": "🍀 You're lucky today!"
}

# ============================================
# HELPER MAGIC
# ============================================

def distance(p1, p2):
    """How far apart are two points in space?"""
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def celebrate(achievement):
    """You did something awesome!"""
    if achievement in trophies and achievement not in you["trophies"]:
        you["trophies"].append(achievement)
        print(f"\n🎉 {trophies[achievement]} 🎉\n")
        time.sleep(0.3)

def crew_growth(amount):
    """Your crew learns and grows!"""
    for person in crew:
        person["xp"] += amount
        if person["xp"] >= person["level"] * 100:
            person["xp"] = 0
            person["level"] += 1
            print(f"\n🎉 {person['name']} is now level {person['level']}!")
            you["credits"] += random.randint(100, 300)

# NEW: Daily luck system
def check_daily_luck():
    today = datetime.now().date()
    if you["last_play"] != str(today):
        you["luck"] = random.randint(1, 10)
        you["last_play"] = str(today)
        print(f"\n🍀 Today's luck: {'⭐' * you['luck']}")
        if you["luck"] >= 8:
            print("🌟 You feel extra lucky today!")
            celebrate("lucky")
        elif you["luck"] >= 5:
            print("✨ It's a good day for adventures!")
        else:
            print("🌙 Maybe stay safe today...")
        time.sleep(0.5)

# NEW: Find a space pet!
def find_pet():
    pet = random.choice(space_pets)
    if pet not in you["pets"]:
        you["pets"].append(pet)
        print(f"\n🐾 A {pet} has joined your crew! How cute!")
        celebrate("pet")
        you["morale"] = min(100, you["morale"] + 10)
    else:
        print(f"\n🐾 {pet} is already part of your crew!")

# NEW: Tell a joke!
def tell_joke():
    joke = random.choice(jokes)
    print(f"\n😂 {joke}\n")
    you["morale"] = min(100, you["morale"] + 5)
    print(f"😊 Crew morale +5! (Now: {you['morale']}%)")

# ============================================
# WHAT YOU CAN DO
# ============================================

def pick_destination():
    """Where do you want to go?"""
    print("\n🪐 WHERE TO?")
    for n, (name, _) in PLANETS.items():
        print(f"{n}. {name}")
    
    def choose(question):
        while True:
            try:
                choice = int(input(question))
                if choice in PLANETS:
                    return PLANETS[choice]
                print("That planet doesn't exist!")
            except:
                print("Please enter a number!")
    
    start = choose("Where are you starting from? ")
    end = choose("Where are you going to? ")
    return start, end

def go_on_mission():
    """Your main adventure!"""
    check_daily_luck()
    
    print("\n🚀 PREPARING FOR LAUNCH!")
    print("1. Travel to known planets")
    print("2. Explore unknown space")
    
    choice = input("Choice: ")
    
    if choice == "1":
        start = pick_destination()
        end = pick_destination()
        start_name = "Your Location"
        end_name = "Destination"
    else:
        try:
            start = (float(input("Start x: ")), float(input("Start y: ")))
            end = (float(input("End x: ")), float(input("End y: ")))
            start_name, end_name = "Unknown", "Unknown"
        except:
            print("❌ Invalid coordinates!")
            return
    
    # Calculate your journey
    dist = distance(start, end)
    print(f"\n📏 {start_name} to {end_name}: {dist:.0f} million km")
    
    # New record?
    if dist > you["record"]:
        you["record"] = dist
        print("🏆 That's your longest trip yet!")
    
    # Space surprises with luck bonus!
    if random.random() < 0.25 + (you["luck"] * 0.01):
        event = random.choice(["wormhole", "treasure", "pet", "joke"])
        if event == "wormhole":
            dist *= 0.6
            print("🌀 You found a wormhole shortcut!")
        elif event == "treasure":
            bonus = random.randint(100, 300) + (you["luck"] * 10)
            you["credits"] += bonus
            print(f"💰 Found space treasure! +{bonus} credits!")
        elif event == "pet":
            find_pet()
        elif event == "joke":
            tell_joke()
    
    # Fuel check
    needed = dist * 0.5
    if you["fuel"] < needed:
        print(f"\n⛽ Uh oh! Need {needed:.0f} fuel, have {you['fuel']:.0f}")
        fuel_choice = input("1. Mine asteroid  2. Buy fuel: ")
        if fuel_choice == "1":
            if random.random() < 0.6 + (you["luck"] * 0.02):
                gained = random.randint(200, 800)
                you["fuel"] += gained
                print(f"✅ Mined {gained} fuel!")
            else:
                lost = random.randint(50, 200)
                you["fuel"] = max(0, you["fuel"] - lost)
                print(f"💥 Ouch! Asteroid damaged your ship! Lost {lost} fuel")
        elif fuel_choice == "2":
            try:
                amount = int(input("How much fuel? "))
                cost = amount * 2
                if you["credits"] >= cost:
                    you["credits"] -= cost
                    you["fuel"] += amount
                    print(f"✅ Bought {amount} fuel!")
                else:
                    print("❌ Not enough credits!")
            except:
                print("❌ Invalid amount!")
        return
    
    # Mission success!
    you["fuel"] -= needed
    earned = int(dist * 0.8 + 50 + (you["luck"] * 2))
    you["credits"] += earned
    you["missions"] += 1
    you["streak"] += 1
    you["morale"] = min(100, you["morale"] + random.randint(5, 15))
    
    print(f"\n✅ MISSION COMPLETE! +{earned} credits")
    print(f"⛽ Fuel left: {you['fuel']:.0f}")
    print(f"😊 Crew morale: {you['morale']}%")
    
    # Random chance to find a pet on mission
    if random.random() < 0.05:
        find_pet()
    
    # Check for achievements
    if you["missions"] == 1: celebrate("first")
    if you["credits"] >= 10000: celebrate("rich")
    if you["missions"] >= 50: celebrate("legend")
    if you["streak"] >= 5: celebrate("streak")
    
    crew_growth(20)

def hunt_bounty():
    """Catch space criminals for money!"""
    check_daily_luck()
    
    print("\n💰 BOUNTY HUNTING")
    print(f"🏆 Your rank: {you['rank']}")
    
    available = [b for b in bounties if b["level"] <= you["rank"] + 1]
    if not available:
        print("No bounties right now. Do more missions!")
        return
    
    print("\n🎯 WANTED:")
    for i, target in enumerate(available[:3], 1):
        print(f"{i}. {target['name']} - 💰 {target['reward']}")
    
    choice = input("Who do you want? (number or 'q'): ")
    if not choice.isdigit() or int(choice) > len(available[:3]):
        return
    
    target = available[int(choice)-1]
    print(f"\n⚔️ FIGHTING {target['name']}...")
    time.sleep(0.5)
    
    my_hp = target["hp"] + (you["luck"] // 3)
    their_hp = target["hp"]
    
    print(f"💪 Luck bonus: +{you['luck']//3} extra health!")
    
    while my_hp > 0 and their_hp > 0:
        print(f"\n❤️ You: {my_hp} | {target['name']}: {their_hp}")
        action = input("1. Attack  2. Dodge: ")
        
        if action == "1":
            damage = random.randint(2, 6) + (you["luck"] // 5)
            their_hp -= damage
            print(f"⚡ You hit for {damage}!")
            if their_hp > 0:
                counter = random.randint(1, 4)
                my_hp -= counter
                print(f"💥 They hit back for {counter}!")
        elif action == "2":
            if random.random() < 0.5 + (you["luck"] * 0.02):
                print("🛡️ You dodged!")
            else:
                counter = random.randint(2, 5)
                my_hp -= counter
                print(f"💥 Too slow! Took {counter} damage!")
        else:
            print("Invalid action!")
    
    if my_hp > 0:
        reward_bonus = int(target["reward"] * (1 + you["luck"] * 0.01))
        you["credits"] += reward_bonus
        print(f"\n🎉 VICTORY! +{reward_bonus} credits! (Luck bonus included)")
        if target["level"] == you["rank"]:
            you["rank"] += 1
            print(f"🏆 Rank up! Now {you['rank']}")
        celebrate("bounty")
        crew_growth(30)
    else:
        print("\n💀 You lost! Lost 100 credits")
        you["credits"] = max(0, you["credits"] - 100)

def do_research():
    """Unlock cool technology!"""
    print("\n🧪 RESEARCH LAB")
    print(f"📚 Points: {you['research']}")
    
    for i, (name, data) in enumerate(tech.items(), 1):
        status = "✅" if data["owned"] else f"💰 {data['cost']}pts"
        print(f"{i}. {name} - {status}")
    print("4. Convert 100 credits → 20 points")
    
    choice = input("What to research? (number): ")
    if choice.isdigit() and 1 <= int(choice) <= 3:
        name, data = list(tech.items())[int(choice)-1]
        if not data["owned"] and you["research"] >= data["cost"]:
            you["research"] -= data["cost"]
            data["owned"] = True
            print(f"✨ UNLOCKED {name}!")
            celebrate("research")
        else:
            print("❌ Not enough points or already owned!")
    elif choice == "4":
        if you["credits"] >= 100:
            you["credits"] -= 100
            you["research"] += 20
            print("✅ Converted credits to research!")
        else:
            print("❌ Not enough credits!")

def trade_with_aliens():
    """Meet space friends and trade!"""
    print("\n👽 ALIEN ENCOUNTER!")
    print(f"💰 Credits: {you['credits']}")
    
    items = {
        "🌌 Crystal": 500,
        "💫 Warp Core": 2000,
        "🔮 Shield": 1500,
        "🍕 Space Pizza": 50
    }
    
    for i, (item, price) in enumerate(items.items(), 1):
        print(f"{i}. {item} - {price}")
    
    choice = input("Buy (number) or 'q': ")
    if choice.isdigit() and 1 <= int(choice) <= len(items):
        item, price = list(items.items())[int(choice)-1]
        if you["credits"] >= price:
            you["credits"] -= price
            you["stuff"].append(item)
            print(f"✨ Bought {item}!")
        else:
            print("❌ Not enough credits!")

def explore_nebula():
    """Fly into colorful space clouds!"""
    nebulae = {"Orion": (1340,-220), "Eagle": (7000,0), "Helix": (695,280)}
    
    print("\n🌌 NEBULA EXPLORATION")
    for i, name in enumerate(nebulae.keys(), 1):
        print(f"{i}. {name}")
    
    choice = input("Where to? (number): ")
    if choice.isdigit() and 1 <= int(choice) <= len(nebulae):
        name = list(nebulae.keys())[int(choice)-1]
        print(f"\n🚀 Flying into {name}...")
        time.sleep(1)
        
        if random.random() < 0.6 + (you["luck"] * 0.02):
            fuel_found = random.randint(300, 1500) + (you["luck"] * 10)
            you["fuel"] += fuel_found
            print(f"⛽ Found {fuel_found} fuel!")
            celebrate("fuel")
        else:
            treasure = random.choice(["relic", "crystal", "chart"])
            you["stuff"].append(treasure)
            print(f"🔮 Found {treasure}!")
            you["research"] += 20 + (you["luck"] * 2)
        
        # Chance to find a pet in nebula
        if random.random() < 0.08:
            find_pet()
    else:
        print("Invalid choice!")

def show_stats():
    """How's your space journey going?"""
    print("\n" + "="*50)
    print("📊 YOUR SPACE JOURNEY")
    print("="*50)
    print(f"🚀 Missions: {you['missions']}")
    print(f"🔥 Streak: {you['streak']}")
    print(f"⛽ Fuel: {you['fuel']:.0f}")
    print(f"💰 Credits: {you['credits']}")
    print(f"📚 Research: {you['research']}")
    print(f"😊 Morale: {you['morale']}%")
    print(f"🏆 Bounty Rank: {you['rank']}")
    print(f"📏 Furthest: {you['record']:.0f} million km")
    print(f"🍀 Luck: {'⭐' * you['luck']}")
    print(f"🏅 Achievements: {len(you['trophies'])}")
    
    if you["trophies"]:
        print("\n🏅 Your trophies:")
        for t in you["trophies"]:
            print(f"  • {trophies[t]}")
    
    if you["pets"]:
        print("\n🐾 Your space pets:")
        for pet in you["pets"]:
            print(f"  • {pet}")
    
    if you["stuff"]:
        print("\n📦 Your stuff:")
        for item in you["stuff"]:
            print(f"  • {item}")

def show_crew():
    """Meet your space family!"""
    print("\n👥 YOUR CREW")
    for person in crew:
        print(f"• {person['name']} - Level {person['level']} ({person['skill']})")
        print(f"  XP: {person['xp']}/{person['level']*100}")

def save_game():
    """Save your adventure to continue later"""
    data = {
        "fuel": you["fuel"], "credits": you["credits"],
        "missions": you["missions"], "streak": you["streak"],
        "morale": you["morale"], "research": you["research"],
        "rank": you["rank"], "record": you["record"],
        "trophies": you["trophies"], "stuff": you["stuff"],
        "pets": you["pets"], "luck": you["luck"],
        "last_play": you["last_play"], "crew": crew
    }
    try:
        with open("space_save.json", "w") as f:
            json.dump(data, f)
        print("💾 Adventure saved!")
    except:
        print("❌ Could not save!")

def load_game():
    """Continue your space journey"""
    global you, crew
    try:
        with open("space_save.json", "r") as f:
            data = json.load(f)
        
        for key in data:
            if key in you and key != "trophies" and key != "stuff" and key != "pets":
                you[key] = data[key]
        you["trophies"] = data.get("trophies", [])
        you["stuff"] = data.get("stuff", [])
        you["pets"] = data.get("pets", [])
        crew[:] = data.get("crew", crew)
        
        print("📀 Welcome back, Captain!")
        return True
    except:
        print("❌ No saved game found!")
        return False

# NEW: Fun menu option - do something random!
def random_fun():
    print("\n🎲 RANDOM FUN!")
    print("="*40)
    options = [
        "tell_joke",
        "find_pet",
        "check_daily_luck",
        "find_treasure"
    ]
    choice = random.choice(options)
    
    if choice == "tell_joke":
        tell_joke()
    elif choice == "find_pet":
        find_pet()
    elif choice == "check_daily_luck":
        check_daily_luck()
    elif choice == "find_treasure":
        treasure = random.randint(50, 200) + (you["luck"] * 5)
        you["credits"] += treasure
        print(f"\n💰 You found {treasure} credits floating in space!")

# ============================================
# LET'S GO!
# ============================================

def main():
    print("""
    ╔══════════════════════════════════════════╗
    ║   🚀 SPACE DISTANCE CALCULATOR 🚀       ║
    ║      The Friendly Space Adventure!      ║
    ║           Version 3.5                   ║
    ║                                         ║
    ║   "The cosmos is yours to explore!"     ║
    ╚══════════════════════════════════════════╝
    """)
    
    print("🌟 Welcome, Captain! The galaxy awaits!\n")
    check_daily_luck()
    
    while True:
        print("\n" + "="*40)
        print("🌟 WHAT'S NEXT?")
        print("="*40)
        print("1. 🚀 Fly a mission")
        print("2. 📊 Check stats")
        print("3. 👥 Meet crew")
        print("4. 🧪 Research")
        print("5. 💰 Hunt bounty")
        print("6. 👽 Trade with aliens")
        print("7. 🌌 Explore nebula")
        print("8. 💾 Save")
        print("9. 📀 Load")
        print("10. 🎲 Random fun")
        print("11. ❌ Quit")
        
        choice = input("\nYour choice: ")
        
        if choice == "1": go_on_mission()
        elif choice == "2": show_stats()
        elif choice == "3": show_crew()
        elif choice == "4": do_research()
        elif choice == "5": hunt_bounty()
        elif choice == "6": trade_with_aliens()
        elif choice == "7": explore_nebula()
        elif choice == "8": save_game()
        elif choice == "9": load_game()
        elif choice == "10": random_fun()
        elif choice == "11":
            print("\n👋 Farewell, Captain! The stars will miss you!")
            print("⭐ Live long and prosper! 🖖")
            break
        else:
            print("❌ Hmm, that's not a valid choice. Try again!")

if __name__ == "__main__":
    main()
