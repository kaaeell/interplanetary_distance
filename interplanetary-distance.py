import math
import random
import time
from datetime import datetime
import json
import os

# SPACE DISTANCE CALCULATOR - ULTIMATE EDITION v2.0
# New today: Space anomalies, research system, bounty hunting, and more!

# ============= GLOBAL VARIABLES =============
history = []
total_calculations = 0
highest_distance = 0
missions_completed = 0
fuel = 5000
credits_total = 1000
achievements = []
inventory = []
crew_morale = 80
consecutive_missions = 0
research_points = 0  # NEW: Research system!
bounty_hunting_level = 1  # NEW: Bounty hunting rank!
discovered_anomalies = []  # NEW: Space anomalies discovered!
last_pirate_defeated = None  # NEW: For bounty system

# ============= DATA SETS =============
galaxy_names = ["Milky Way","Andromeda","Sombrero Galaxy","Whirlpool Galaxy","Black Eye Galaxy","Cartwheel Galaxy","Triangulum Galaxy","Pinwheel Galaxy"]
astronauts = ["Neil","Buzz","Sally","Yuri","Mae","Chris","Valentina","Jose","Priya","Chen"]
spaceships = ["StarRunner","NovaX","Galaxy Rider","Void Explorer","Cosmic Storm","Nebula One","Quantum Leap","Starlight"]
space_pets = ["space dog","robot cat","alien hamster","tiny moon dragon","quantum parrot","zero-g fish"]
badges = ["🌟 rookie pilot","🚀 master explorer","🪐 galaxy navigator","☄️ asteroid survivor","🔭 deep space observer","⚡ speed champion"]
alien_names = ["Zorg","Xenon","Blip","Nova","Kratos","Glimmer","Vortex","Stardust"]
space_foods = ["freeze dried pizza","space tacos","galaxy noodles","moon burgers","asteroid ice cream","nebula smoothie"]
space_jobs = ["pilot","engineer","galaxy scout","alien translator","space mechanic","astrobiologist","warp specialist"]
planet_conditions = ["lava storms","ice surface","heavy gravity","safe landing","radioactive atmosphere","crystal caves","underwater cities"]

comet_names = ["Halley","Encke","Hale-Bopp","Swift-Tuttle","Neowise","Lovejoy","ISON"]
space_jokes = [
    "Why did the star go to school? To get a little brighter!",
    "What do astronauts use to keep their pants up? An asteroid belt!",
    "Why don't aliens visit our solar system? They read the reviews… only one star!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key on a keyboard? The space bar!"
]
alien_greetings = ["👽 Blip blop!","👾 Greetings Earthling!","🛸 Take me to your leader!","🛸 Beep boop!","🌌 We come in peace!","✨ Hello from Andromeda!"]

# ============= NEW: SPACE ANOMALIES =============
space_anomalies = {
    "🔄 Time Dilation Field": {
        "description": "Time moves differently here!",
        "effect": "bonus_research",
        "reward": 50
    },
    "🌀 Quantum Rift": {
        "description": "Reality is unstable!",
        "effect": "teleport",
        "reward": None
    },
    "✨ Sentient Nebula": {
        "description": "The nebula is alive!",
        "effect": "gift",
        "reward": 300
    },
    "⚫ Micro Black Hole": {
        "description": "Tiny but dangerous!",
        "effect": "danger",
        "damage": 150
    },
    "🎵 Space Whale Song": {
        "description": "Beautiful cosmic whales singing!",
        "effect": "morale_boost",
        "reward": 20
    },
    "📜 Ancient Ruins": {
        "description": "Remains of an old civilization!",
        "effect": "artifact",
        "reward": None
    }
}

# ============= NEW: BOUNTY TARGETS =============
bounty_targets = [
    {"name": "Red Pirate", "bounty": 500, "level": 1, "health": 3},
    {"name": "Shadow Corsair", "bounty": 1000, "level": 2, "health": 5},
    {"name": "Void Reaver", "bounty": 2000, "level": 3, "health": 7},
    {"name": "Star Eater", "bounty": 5000, "level": 4, "health": 10},
    {"name": "Galactic Menace", "bounty": 10000, "level": 5, "health": 15}
]

# ============= RESEARCH UPGRADES =============
research_upgrades = {
    "Fuel Efficiency": {"cost": 100, "effect": "fuel_consumption", "value": 0.9, "owned": False},
    "Warp Drive": {"cost": 200, "effect": "speed_bonus", "value": 1.2, "owned": False},
    "Shield Tech": {"cost": 150, "effect": "damage_reduction", "value": 0.7, "owned": False},
    "Scanner Range": {"cost": 120, "effect": "credit_bonus", "value": 1.3, "owned": False},
    "Quantum Shields": {"cost": 300, "effect": "critical_protection", "value": 0.5, "owned": False}
}

achievement_list = {
    "first_step": "🌱 First Step - Complete your first mission",
    "milky_way_tourist": "🌌 Milky Way Tourist - Travel over 2000 million km",
    "fuel_hunter": "⛽ Fuel Hunter - Collect fuel from a nebula",
    "alien_friend": "👽 Alien Friend - Successfully trade with aliens",
    "millionaire": "💰 Space Millionaire - Earn 10,000 credits",
    "speed_demon": "⚡ Speed Demon - Complete a mission in under 30 seconds",
    "badge_collector": "🎖️ Badge Collector - Earn 5 different badges",
    "pet_lover": "🐾 Pet Lover - Adopt a space pet",
    "galaxy_legend": "⭐ Galaxy Legend - Complete 50 missions",
    "streak_master": "🔥 Streak Master - Complete 5 missions in a row",
    "wormhole_rider": "🌀 Wormhole Rider - Successfully use a wormhole",
    "anomaly_hunter": "🔭 Anomaly Hunter - Discover 3 space anomalies",  # NEW
    "bounty_hunter": "💰 Bounty Hunter - Defeat a bounty target",  # NEW
    "research_genius": "🧠 Research Genius - Unlock 3 research upgrades",  # NEW
    "space_whisperer": "🐋 Space Whisperer - Find the space whales",  # NEW
    "comet_chaser": "☄️ Comet Chaser - Track a comet",  # NEW
    "galactic_hero": "🦸 Galactic Hero - Reach bounty rank 5"  # NEW
}

nebulae = {
    "Orion Nebula": (1340, -220),
    "Eagle Nebula": (7000, 0),
    "Helix Nebula": (695, 280),
    "Crab Nebula": (6500, 190),
    "Tarantula Nebula": (160000, 5000),
    "Horsehead Nebula": (1500, -300),  # NEW
    "Cat's Eye Nebula": (3000, 400)  # NEW
}

alien_items = {
    "🌌 dark matter crystal": 500,
    "💫 warp core upgrade": 2000,
    "🔮 quantum shield": 1500,
    "🍕 exotic space pizza": 50,
    "🐉 baby space dragon egg": 3000,
    "📡 anomaly scanner": 800,  # NEW
    "🔭 research data": 400  # NEW
}

# ============= RANDOM EVENTS =============
random_events = [
    {"name": "🌀 WORMHOLE!", "effect": "shortcut", "message": "You found a wormhole! Distance reduced by 40%!", "modifier": 0.6},
    {"name": "🏴‍☠️ SPACE PIRATES!", "effect": "danger", "message": "Space pirates attacked! Lost 200 fuel and 100 credits!", "fuel": -200, "credits": -100},
    {"name": "✨ COSMIC CACHE", "effect": "reward", "message": "Found a floating cargo pod! +300 credits and +150 fuel!", "fuel": 150, "credits": 300},
    {"name": "🌊 SOLAR FLARE", "effect": "danger", "message": "Solar flare damaged shields! Lost 100 fuel!", "fuel": -100},
    {"name": "🤝 FRIENDLY ALIENS", "effect": "reward", "message": "Friendly aliens gave you a gift! +250 credits!", "credits": 250},
    {"name": "📡 MYSTERY SIGNAL", "effect": "anomaly", "message": "Strange signal detected!", "anomaly": True},  # NEW
    {"name": "☄️ COMET FLYBY", "effect": "comet", "message": "A comet is passing by!", "comet": True}  # NEW
]

# ============= CORE FUNCTIONS =============
def calculate_distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def get_coordinates(name):
    while True:
        try:
            print(f"\nEnter coordinates for {name} (in million km)")
            x = float(input("x: "))
            y = float(input("y: "))
            return (x, y)
        except ValueError:
            print("invalid input")

def choose_planets():
    planets = {
        1: ("Earth",(0,0)), 2: ("Mars",(225,0)), 3: ("Venus",(108,0)), 4: ("Jupiter",(778,0)),
        5: ("Saturn",(1427,0)), 6: ("Uranus",(2871,0)), 7: ("Neptune",(4495,0)), 8: ("Mercury",(58,0)),
        9: ("Pluto",(5906,0)), 10: ("Moon",(1,0))
    }
    print("\n📋 Available planets:")
    for num, (name, _) in planets.items():
        print(f"{num}. {name}")
    def pick(msg):
        while True:
            try:
                choice = int(input(msg))
                if choice in planets:
                    return planets[choice]
                else:
                    print("pick a valid number")
            except ValueError:
                print("numbers only")
    p1_name, p1 = pick("Choose planet 1: ")
    p2_name, p2 = pick("Choose planet 2: ")
    return p1_name, p1, p2_name, p2

# ============= NEW: ANOMALY DISCOVERY SYSTEM =============
def discover_anomaly():
    global research_points, crew_morale, fuel, credits_total, inventory
    
    anomaly_name = random.choice(list(space_anomalies.keys()))
    anomaly = space_anomalies[anomaly_name]
    
    print(f"\n🔭 ANOMALY DISCOVERED: {anomaly_name} 🔭")
    print(f"📖 {anomaly['description']}")
    
    if anomaly_name not in discovered_anomalies:
        discovered_anomalies.append(anomaly_name)
        print(f"✨ New anomaly added to discovery log!")
        if len(discovered_anomalies) >= 3:
            check_achievement("anomaly_hunter")
    
    if anomaly["effect"] == "bonus_research":
        gain = anomaly["reward"]
        research_points += gain
        print(f"🧠 +{gain} research points!")
        
    elif anomaly["effect"] == "teleport":
        print("🌀 You've been teleported to a random location!")
        print("(Your next mission might be affected!)")
        
    elif anomaly["effect"] == "gift":
        gain = anomaly["reward"]
        credits_total += gain
        print(f"💰 The anomaly gave you {gain} credits!")
        
    elif anomaly["effect"] == "danger":
        damage = anomaly["damage"]
        fuel = max(0, fuel - damage)
        print(f"💥 You lost {damage} fuel escaping!")
        
    elif anomaly["effect"] == "morale_boost":
        gain = anomaly["reward"]
        crew_morale = min(100, crew_morale + gain)
        print(f"😊 Crew morale +{gain}! (Now: {crew_morale}%)")
        if anomaly_name == "🎵 Space Whale Song":
            check_achievement("space_whisperer")
            
    elif anomaly["effect"] == "artifact":
        artifact = random.choice(["ancient tablet", "crystal skull", "energy orb", "star map"])
        inventory.append(artifact)
        print(f"🔮 You found an {artifact}!")
        research_points += 30
        print(f"🧠 +30 research points from studying the artifact!")

# ============= NEW: BOUNTY HUNTING SYSTEM =============
def bounty_hunting():
    global credits_total, fuel, bounty_hunting_level, last_pirate_defeated
    
    print("\n💰 BOUNTY HUNTING SYSTEM 💰")
    print(f"🏆 Your Bounty Rank: {bounty_hunting_level}")
    
    available_targets = [t for t in bounty_targets if t["level"] <= bounty_hunting_level + 1]
    
    if not available_targets:
        print("No available bounties at your rank! Complete more missions!")
        return
    
    print("\n🎯 AVAILABLE BOUNTIES:")
    for i, target in enumerate(available_targets[:3], 1):
        print(f"{i}. {target['name']} - 💰 {target['bounty']} credits (Level {target['level']})")
    
    choice = input("\nSelect bounty (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(available_targets[:3]):
        target = available_targets[int(choice)-1]
        
        print(f"\n🚀 Hunting {target['name']}...")
        time.sleep(1)
        
        # Simple combat mini-game
        print("⚔️ COMBAT MODE ⚔️")
        player_health = target['health']
        target_health = target['health']
        
        while player_health > 0 and target_health > 0:
            print(f"\n❤️ Your health: {player_health} | {target['name']} health: {target_health}")
            action = input("1. Attack | 2. Dodge | 3. Use item: ")
            
            if action == "1":
                damage = random.randint(2, 6)
                target_health -= damage
                print(f"⚡ You dealt {damage} damage!")
                
                # Enemy counterattack
                enemy_damage = random.randint(1, 5)
                player_health -= enemy_damage
                print(f"💥 {target['name']} dealt {enemy_damage} damage!")
                
            elif action == "2":
                if random.random() < 0.6:
                    print("🛡️ You dodged the attack!")
                else:
                    enemy_damage = random.randint(2, 6)
                    player_health -= enemy_damage
                    print(f"💥 Failed to dodge! Took {enemy_damage} damage!")
                    
            elif action == "3":
                print("🩹 Using repair kit...")
                heal = random.randint(3, 8)
                player_health = min(target['health'], player_health + heal)
                print(f"❤️ Restored {heal} health!")
        
        if player_health > 0:
            reward = target['bounty']
            credits_total += reward
            print(f"\n🎉 VICTORY! Defeated {target['name']}!")
            print(f"💰 Claimed {reward} credits!")
            
            if target["level"] == bounty_hunting_level:
                bounty_hunting_level = min(5, bounty_hunting_level + 1)
                print(f"🏆 Bounty rank increased to {bounty_hunting_level}!")
                
            check_achievement("bounty_hunter")
            if bounty_hunting_level >= 5:
                check_achievement("galactic_hero")
        else:
            print(f"\n💀 Defeated by {target['name']}... Lost 200 credits")
            credits_total = max(0, credits_total - 200)

# ============= NEW: RESEARCH SYSTEM =============
def research_lab():
    global research_points, fuel, credits_total
    
    print("\n🧪 RESEARCH LAB 🧪")
    print(f"📚 Research Points: {research_points}")
    print("\nAvailable Upgrades:")
    
    upgrades_list = list(research_upgrades.items())
    for i, (name, data) in enumerate(upgrades_list, 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} RP"
        print(f"{i}. {name} - {status}")
    
    print("\n7. Convert credits to research points (100 credits = 20 RP)")
    
    choice = input("\nSelect upgrade (number) or 'quit': ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(upgrades_list):
        upgrade_name, upgrade_data = upgrades_list[int(choice)-1]
        if not upgrade_data["owned"]:
            if research_points >= upgrade_data["cost"]:
                research_points -= upgrade_data["cost"]
                upgrade_data["owned"] = True
                print(f"✨ Unlocked {upgrade_name}! ✨")
                check_achievement("research_genius")
            else:
                print(f"❌ Need {upgrade_data['cost']} research points!")
        else:
            print("❌ Already owned!")
            
    elif choice == "7":
        amount = int(input("How many credits to convert? "))
        if amount >= 100:
            rp_gain = (amount // 100) * 20
            credits_total -= amount
            research_points += rp_gain
            print(f"✨ Converted {amount} credits into {rp_gain} research points!")

# ============= NEW: COMET TRACKING =============
def track_comet():
    global credits_total, research_points
    
    print("\n☄️ COMET TRACKING SYSTEM ☄️")
    comet = random.choice(comet_names)
    print(f"Tracking comet {comet}...")
    time.sleep(1)
    
    # Simple telescope mini-game
    print("\nAdjust your telescope!")
    target_angle = random.randint(0, 360)
    print(f"Target angle: ???")
    
    guess = int(input("Your guess (0-360): "))
    difference = min(abs(guess - target_angle), 360 - abs(guess - target_angle))
    
    if difference < 10:
        reward = 500
        print(f"🎯 PERFECT! You found comet {comet}!")
        print(f"💰 +{reward} credits!")
        credits_total += reward
        research_points += 30
        check_achievement("comet_chaser")
    elif difference < 30:
        reward = 200
        print(f"👍 Good! You spotted comet {comet}!")
        print(f"💰 +{reward} credits!")
        credits_total += reward
        research_points += 15
    else:
        print(f"😅 Missed it! The comet was at {target_angle}°")

# ============= NEW: SAVE/LOAD SYSTEM =============
def save_game():
    save_data = {
        "history": history,
        "total_calculations": total_calculations,
        "highest_distance": highest_distance,
        "missions_completed": missions_completed,
        "fuel": fuel,
        "credits_total": credits_total,
        "achievements": achievements,
        "inventory": inventory,
        "crew_morale": crew_morale,
        "consecutive_missions": consecutive_missions,
        "research_points": research_points,
        "bounty_hunting_level": bounty_hunting_level,
        "discovered_anomalies": discovered_anomalies,
        "research_upgrades_owned": {name: data["owned"] for name, data in research_upgrades.items()}
    }
    
    with open("space_save.json", "w") as f:
        json.dump(save_data, f)
    print("💾 Game saved successfully!")

def load_game():
    global history, total_calculations, highest_distance, missions_completed, fuel, credits_total
    global achievements, inventory, crew_morale, consecutive_missions, research_points
    global bounty_hunting_level, discovered_anomalies
    
    try:
        with open("space_save.json", "r") as f:
            save_data = json.load(f)
        
        history = save_data.get("history", [])
        total_calculations = save_data.get("total_calculations", 0)
        highest_distance = save_data.get("highest_distance", 0)
        missions_completed = save_data.get("missions_completed", 0)
        fuel = save_data.get("fuel", 5000)
        credits_total = save_data.get("credits_total", 1000)
        achievements = save_data.get("achievements", [])
        inventory = save_data.get("inventory", [])
        crew_morale = save_data.get("crew_morale", 80)
        consecutive_missions = save_data.get("consecutive_missions", 0)
        research_points = save_data.get("research_points", 0)
        bounty_hunting_level = save_data.get("bounty_hunting_level", 1)
        discovered_anomalies = save_data.get("discovered_anomalies", [])
        
        # Load research upgrades
        upgrades_owned = save_data.get("research_upgrades_owned", {})
        for name, owned in upgrades_owned.items():
            if name in research_upgrades:
                research_upgrades[name]["owned"] = owned
        
        print("📀 Game loaded successfully!")
        return True
    except FileNotFoundError:
        print("❌ No save file found!")
        return False

# ============= EXISTING FUNCTIONS (enhanced) =============
def trigger_random_event():
    global fuel, credits_total, consecutive_missions
    
    if random.random() < 0.35:  # Increased chance!
        event = random.choice(random_events)
        print(f"\n⚠️ EVENT: {event['name']} ⚠️")
        print(event['message'])
        
        if event.get('anomaly'):
            discover_anomaly()
            return 1.0
            
        if event.get('comet'):
            track_comet()
            return 1.0
        
        if 'modifier' in event:
            return event['modifier']
            
        if 'fuel' in event:
            fuel = max(0, fuel + event['fuel'])
        if 'credits' in event:
            credits_total = max(0, credits_total + event['credits'])
        
        if event['name'] == "🌀 WORMHOLE!":
            check_achievement("wormhole_rider")
        
        return 1.0
    return 1.0

def update_crew_morale(distance, success=True):
    global crew_morale, consecutive_missions
    if success:
        gain = random.randint(5, 15)
        crew_morale = min(100, crew_morale + gain)
        consecutive_missions += 1
        print(f"😊 Crew morale +{gain}! (Now: {crew_morale}%)")
        if consecutive_missions >= 5:
            check_achievement("streak_master")
    else:
        loss = random.randint(10, 25)
        crew_morale = max(0, crew_morale - loss)
        consecutive_missions = 0
        print(f"😞 Crew morale -{loss}! (Now: {crew_morale}%)")
    
    if crew_morale > 80:
        print("🎉 Crew is HYPED! Mission bonus active!")
    elif crew_morale < 30:
        print("⚠️ Crew morale critically low! Buy space pizza!")

def show_crew_status():
    bar_length = 20
    filled = int(bar_length * crew_morale / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    mood_emoji = "😄" if crew_morale > 70 else "😐" if crew_morale > 40 else "😞"
    print(f"👥 Morale: [{bar}] {crew_morale}% {mood_emoji}")

def check_fuel(distance):
    global fuel
    # Apply fuel efficiency upgrade if owned
    if research_upgrades["Fuel Efficiency"]["owned"]:
        fuel_needed = distance * 0.5 * research_upgrades["Fuel Efficiency"]["value"]
        print(f"⛽ Fuel efficiency active! Using {fuel_needed:.1f} instead of {distance * 0.5:.1f}")
    else:
        fuel_needed = distance * 0.5
    
    if fuel < fuel_needed:
        print(f"\n⚠️ INSUFFICIENT FUEL! Need {fuel_needed:.1f}, have {fuel:.1f}")
        collect_emergency_fuel()
        return check_fuel(distance)
    else:
        fuel -= fuel_needed
        print(f"⛽ Used: {fuel_needed:.1f} | Remaining: {fuel:.1f}")
        return True

def collect_emergency_fuel():
    global fuel, credits_total
    print("\n🔄 EMERGENCY FUEL COLLECTION 🔄")
    print("1. 🛸 Mine asteroid (risky)")
    print("2. 💰 Buy fuel")
    print("3. 🎲 Space casino")
    
    choice = input("Choose: ")
    
    if choice == "1":
        if random.random() < 0.6:
            gained = random.randint(200, 800)
            fuel += gained
            print(f"✅ +{gained} fuel")
        else:
            damage = random.randint(50, 200)
            fuel = max(0, fuel - damage)
            print(f"💥 Lost {damage} fuel")
    elif choice == "2":
        cost_per_unit = 2
        amount = int(input("Amount to buy: "))
        cost = amount * cost_per_unit
        if credits_total >= cost:
            credits_total -= cost
            fuel += amount
            print(f"✅ Bought {amount} fuel!")
        else:
            print("❌ Not enough credits!")
    elif choice == "3":
        bet = int(input("Bet credits: "))
        if bet > credits_total:
            print("Not enough!")
            return
        if random.random() > 0.7:
            winnings = bet * random.uniform(1.5, 3)
            credits_total += winnings
            fuel += random.randint(100, 400)
            print(f"🎉 WIN! +{winnings:.0f} credits and fuel!")
        else:
            credits_total -= bet
            print(f"💀 Lost {bet} credits!")

def alien_trade():
    global credits_total, inventory
    print("\n🛸 ALIEN TRADING POST 🛸")
    print(f"💰 Credits: {credits_total}")
    items_list = list(alien_items.items())
    for i, (item, price) in enumerate(items_list, 1):
        print(f"{i}. {item} - {price} credits")
    
    choice = input("Buy (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(items_list):
        item, price = items_list[int(choice)-1]
        if credits_total >= price:
            credits_total -= price
            inventory.append(item)
            print(f"✨ Bought {item}!")
            check_achievement("alien_friend")
        else:
            print("❌ Need more credits!")

def explore_nebula():
    global fuel, achievements, research_points
    print("\n🌌 NEBULA EXPLORATION")
    neb_list = list(nebulae.items())
    for i, (name, coords) in enumerate(neb_list[:5], 1):
        print(f"{i}. {name}")
    
    choice = input("Explore (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= 5:
        neb_name, coords = neb_list[int(choice)-1]
        print(f"\n🚀 Warping to {neb_name}...")
        time.sleep(1)
        
        if random.random() < 0.6:
            fuel_gained = random.randint(300, 1500)
            fuel += fuel_gained
            print(f"⛽ Collected {fuel_gained} fuel!")
            check_achievement("fuel_hunter")
            
            # Chance for anomaly in nebula
            if random.random() < 0.3:
                discover_anomaly()
        else:
            artifact = random.choice(["ancient relic", "crystal shard", "energy core", "star chart"])
            inventory.append(artifact)
            print(f"🔮 Found {artifact}!")
            research_points += 20
            print(f"🧠 +20 research points!")

def space_race():
    global credits_total, fuel
    print("\n🏁 SPACE RACE CHALLENGE 🏁")
    print("Race from Earth to Mars!")
    
    input("Press ENTER when ready...")
    print("3... 2... 1...")
    time.sleep(random.uniform(0.5, 2.0))
    print("🟢 GO!")
    start = time.time()
    input()
    reaction = time.time() - start
    
    print(f"Your time: {reaction:.2f} seconds")
    
    if reaction < 0.5:
        winnings = 1000
        print(f"🏆 AMAZING! +{winnings} credits!")
        credits_total += winnings
        check_achievement("speed_demon")
    elif reaction < 1.0:
        winnings = 500
        print(f"👍 Good! +{winnings} credits!")
        credits_total += winnings
    else:
        print("😅 Keep practicing!")

def check_achievement(achievement_key):
    global achievements
    if achievement_key in achievement_list and achievement_key not in achievements:
        achievements.append(achievement_key)
        print(f"\n🏆 ACHIEVEMENT: {achievement_list[achievement_key]} 🏆\n")

def daily_bonus():
    global credits_total, fuel, research_points
    print("\n🎁 DAILY BONUS! 🎁")
    bonus_credits = random.randint(200, 800)
    bonus_fuel = random.randint(100, 300)
    bonus_rp = random.randint(10, 50)
    credits_total += bonus_credits
    fuel += bonus_fuel
    research_points += bonus_rp
    print(f"✨ +{bonus_credits} credits | +{bonus_fuel} fuel | +{bonus_rp} RP")

# ============= FLUFF FUNCTIONS =============
def show_fun_fact():
    facts = ["Venus spins backwards","Mars sunsets are blue","Saturn could float in water","Jupiter is insanely huge","Neptune has crazy strong winds","A day on Venus is longer than a year there","There's a cloud of alcohol in space","One day on Mercury is 59 Earth days"]
    print(f"\n📚 {random.choice(facts)}")

def show_space_event():
    events = ["☄️ comet nearby","🌠 meteor shower","🛰️ deep space signal","👽 aliens watching","🪐 strange rings","✨ shooting star","🌌 galaxy collision far away"]
    print(f"✨ {random.choice(events)}")

def random_space_weather():
    weather = ["☀️ solar calm","🌌 radiation normal","☄️ asteroid traffic","🛰️ satellites fine","⚡ solar storm","🌊 gravity wave","🌀 ion storm"]
    print(f"\n🌦️ {random.choice(weather)}")

def mission_status():
    missions = ["✅ mission complete","🚀 nav online","⚠️ fuel okay","🌌 systems stable","📡 comms active","⚡ power nominal"]
    print(f"📡 {random.choice(missions)}")

def detect_black_hole():
    if random.randint(1, 12) == 1:
        print("🕳️ ⚠️ BLACK HOLE NEARBY! ⚠️")
        global fuel
        fuel -= random.randint(50, 200)
    else:
        print("✅ No black holes detected")

def oxygen_level():
    print(f"🫁 Oxygen: {random.randint(70, 100)}%")

def random_rank(distance):
    if distance > 5000: print("🏆 Intergalactic Traveler")
    elif distance > 3000: print("🏆 Galaxy Traveler")
    elif distance > 1000: print("🏆 Space Explorer")
    elif distance > 300: print("🏆 Orbit Runner")
    else: print("🏆 Moon Walker")

def random_galaxy(): print(f"🌌 Galaxy: {random.choice(galaxy_names)}")
def random_astronaut(): print(f"👨‍🚀 Astronaut: {random.choice(astronauts)}")
def random_spaceship(): print(f"🛸 Ship: {random.choice(spaceships)}")
def distance_category(distance):
    if distance < 100: print("📍 Short trip")
    elif distance < 1000: print("📍 Medium trip")
    elif distance < 3000: print("📍 Long trip")
    else: print("📍 Extreme travel")
def random_signal(): print(random.choice(["📡 Strange signal","📡 Signal stable","📡 Comms delay","📡 Signal lost"]))
def moon_phase(): print(random.choice(["🌕 Full moon","🌗 Half moon","🌑 New moon","🌙 Crescent moon"]))
def crew_mood(): print(random.choice(["😄 Crew happy","😴 Crew tired","🤖 Robots working","🧑‍🚀 Crew excited"]))
def temperature_check(): print(f"🌡️ Temp: {random.randint(-150, 120)}°C")
def danger_level(): print(random.choice(["🟢 Low","🟡 Medium","🟠 High","🔴 Critical"]))
def daily_space_tip(): print(random.choice(["💡 Double-check coordinates","💡 Keep fuel above 30%","💡 Avoid black holes","💡 Nebulae = fuel","💡 Upgrade your ship","💡 Save before risky jumps"]))
def random_space_pet(): 
    pet = random.choice(space_pets)
    print(f"🐾 Pet: {pet}")
    if random.random() < 0.1:
        inventory.append(pet)
        print(f"🎉 {pet} joined your crew!")
        check_achievement("pet_lover")
def random_badge(): 
    badge = random.choice(badges)
    print(f"🎖️ Badge: {badge}")
    if len([b for b in achievements if "badge" in b]) >= 5:
        check_achievement("badge_collector")
def signal_strength(): print(f"📶 Signal: {random.randint(40, 100)}%")
def credits_display(): print(f"💰 Credits: {credits_total}")
def asteroid_scan(): 
    asteroids = random.randint(0, 15)
    print(f"🪨 Asteroids: {asteroids}")
    if asteroids > 10:
        print("⚠️ Heavy asteroid field!")
def alien_encounter(): 
    if random.randint(1, 5) == 1:
        print(f"👽 ALIEN: {random.choice(alien_names)} wants to trade!")
        alien_trade()
    else:
       
