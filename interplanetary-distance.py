import math
import random
import time
from datetime import datetime
import json
import os

# SPACE DISTANCE CALCULATOR - ULTIMATE EDITION v3.4
# Complete version with all features!


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
research_points = 0
bounty_hunting_level = 1
discovered_anomalies = []
last_pirate_defeated = None

# ============= PIRATE RAID DEFENSE =============
pirate_raids = []
defense_turrets = {
    "Laser Turret": {"owned": False, "cost": 500, "damage": 20},
    "Missile Battery": {"owned": False, "cost": 800, "damage": 35},
    "Shield Generator": {"owned": False, "cost": 600, "defense": 20},
    "Plasma Cannon": {"owned": False, "cost": 1200, "damage": 50}
}

pirate_raid_stats = {
    "raids_survived": 0,
    "raids_defeated": 0,
    "total_damage_dealt": 0,
    "total_loot": 0
}

raid_difficulties = [
    {"name": "Small Scout", "health": 50, "damage": 10, "loot": 200},
    {"name": "Marauder", "health": 100, "damage": 20, "loot": 500},
    {"name": "Raider Fleet", "health": 200, "damage": 35, "loot": 1000},
    {"name": "Pirate Lord", "health": 350, "damage": 50, "loot": 2000},
    {"name": "Armada", "health": 500, "damage": 75, "loot": 5000}
]

# ============= DAILY CHALLENGES =============
daily_challenges = []
last_challenge_date = None

challenge_templates = [
    {"name": "Distance Master", "description": "Travel 500 million km", "goal": 500, "reward": 300, "type": "distance"},
    {"name": "Fuel Collector", "description": "Collect 1000 fuel", "goal": 1000, "reward": 200, "type": "fuel"},
    {"name": "Bounty Hunter", "description": "Complete 3 bounties", "goal": 3, "reward": 500, "type": "bounty"},
    {"name": "Star Explorer", "description": "Visit 5 different planets", "goal": 5, "reward": 400, "type": "planets"},
    {"name": "Credit Grinder", "description": "Earn 2000 credits", "goal": 2000, "reward": 600, "type": "credits"},
    {"name": "Research Genius", "description": "Gain 100 research points", "goal": 100, "reward": 350, "type": "research"},
    {"name": "Race Champion", "description": "Win 2 races", "goal": 2, "reward": 450, "type": "races"},
    {"name": "Mining Pro", "description": "Mine 30 resources", "goal": 30, "reward": 400, "type": "mining"},
    {"name": "Colony Builder", "description": "Collect colony income twice", "goal": 2, "reward": 500, "type": "colony"},
    {"name": "Casino Winner", "description": "Win 1000 credits at casino", "goal": 1000, "reward": 300, "type": "casino"},
    {"name": "Pirate Slayer", "description": "Defeat 3 pirate raids", "goal": 3, "reward": 600, "type": "pirate"}
]

daily_progress = {
    "distance": 0,
    "fuel": 0,
    "bounty": 0,
    "planets": 0,
    "credits": 0,
    "research": 0,
    "races": 0,
    "mining": 0,
    "colony": 0,
    "casino": 0,
    "pirate": 0
}

# ============= SPACE CASINO =============
casino_games = {
    "Cosmic Slots": {"min_bet": 10, "max_bet": 500, "jackpot": 5000},
    "Alien Poker": {"min_bet": 20, "max_bet": 1000, "jackpot": 10000},
    "Roulette": {"min_bet": 5, "max_bet": 300, "jackpot": 3000},
    "Black Hole Blackjack": {"min_bet": 15, "max_bet": 800, "jackpot": 8000}
}

casino_stats = {
    "total_bet": 0,
    "total_won": 0,
    "biggest_win": 0,
    "games_played": 0
}

# ============= SPACE RACING LEAGUE =============
race_tracks = [
    {"name": "Asteroid Field Dash", "difficulty": 1, "prize": 300, "record": 60.0},
    {"name": "Saturn's Ring Circuit", "difficulty": 2, "prize": 600, "record": 90.0},
    {"name": "Nebula Run", "difficulty": 3, "prize": 1000, "record": 120.0},
    {"name": "Black Hole Slingshot", "difficulty": 4, "prize": 2000, "record": 150.0},
    {"name": "Galactic Grand Prix", "difficulty": 5, "prize": 5000, "record": 180.0}
]

racing_upgrades = {
    "Nitro Boost": {"owned": False, "cost": 500, "bonus": 0.2},
    "Aero Wings": {"owned": False, "cost": 300, "bonus": 0.1},
    "Quantum Engine": {"owned": False, "cost": 1000, "bonus": 0.3},
    "Shield Deflector": {"owned": False, "cost": 700, "bonus": 0.15}
}

racing_stats = {
    "races_entered": 0,
    "races_won": 0,
    "best_time": 999.0,
    "total_winnings": 0
}

# ============= PLANETARY COLONIZATION =============
colonies = []
available_planets = [
    {"name": "Mars", "cost": 2000, "income": 100, "hazards": ["dust_storms"], "colonized": False},
    {"name": "Europa", "cost": 3000, "income": 150, "hazards": ["ice_cracks"], "colonized": False},
    {"name": "Titan", "cost": 2500, "income": 120, "hazards": ["methane_lakes"], "colonized": False},
    {"name": "Kepler-22b", "cost": 5000, "income": 300, "hazards": ["alien_wildlife"], "colonized": False},
    {"name": "Proxima Centauri b", "cost": 8000, "income": 500, "hazards": ["solar_flares"], "colonized": False}
]

colonization_upgrades = {
    "Defense System": {"cost": 1000, "owned": False, "bonus": 50},
    "Research Lab": {"cost": 800, "owned": False, "bonus": 30},
    "Trade Hub": {"cost": 1500, "owned": False, "bonus": 100},
    "Mining Facility": {"cost": 1200, "owned": False, "bonus": 75}
}

# ============= BLACK MARKET =============
black_market_items = {
    "Stolen Research Data": {"price": 300, "risk": 20, "reward": "research", "value": 80},
    "Illegal Weapons": {"price": 500, "risk": 40, "reward": "combat", "value": 150},
    "Alien Tech": {"price": 1000, "risk": 60, "reward": "tech", "value": 300},
    "Black Hole Fragment": {"price": 2000, "risk": 80, "reward": "special", "value": 800},
    "Forgotten Map": {"price": 400, "risk": 30, "reward": "treasure", "value": 200}
}

smuggling_heat = 0
black_market_access = False

# ============= DIPLOMATIC RELATIONS =============
alien_factions = {
    "Crystal Collective": {"relation": 50, "benefits": [], "trade_discount": 0},
    "Nebula Nomads": {"relation": 50, "benefits": [], "trade_discount": 0},
    "Star Empire": {"relation": 50, "benefits": [], "trade_discount": 0},
    "Void Syndicate": {"relation": 50, "benefits": [], "trade_discount": 0}
}

# ============= CREW SKILL SYSTEM =============
crew_members = [
    {"name": "Captain", "skill": "Leadership", "level": 1, "xp": 0, "bonus": "morale"},
    {"name": "Engineer", "skill": "Mechanics", "level": 1, "xp": 0, "bonus": "fuel_saving"},
    {"name": "Navigator", "skill": "Astrogation", "level": 1, "xp": 0, "bonus": "distance_bonus"},
    {"name": "Scientist", "skill": "Research", "level": 1, "xp": 0, "bonus": "rp_bonus"},
    {"name": "Gunner", "skill": "Combat", "level": 1, "xp": 0, "bonus": "combat_damage"}
]

# ============= SPACE STOCK MARKET =============
stock_market = {
    "Space Fuel": {"price": 100, "volatility": 0.15, "owned": 0},
    "Dark Matter": {"price": 500, "volatility": 0.25, "owned": 0},
    "Alien Artifacts": {"price": 300, "volatility": 0.2, "owned": 0},
    "Quantum Chips": {"price": 200, "volatility": 0.18, "owned": 0},
    "Nebula Gas": {"price": 80, "volatility": 0.12, "owned": 0}
}

market_news = [
    "📰 New mining operation discovered!",
    "📰 Alien trade routes disrupted!",
    "📰 Space pirates attacking convoys!",
    "📰 Research breakthrough announced!",
    "📰 Government subsidies approved!",
    "📰 Supply shortage reported!"
]

# ============= SPACE MINING SYSTEM =============
mining_resources = {
    "Iron Ore": {"value": 50, "difficulty": 1, "yield": (10, 30)},
    "Titanium": {"value": 120, "difficulty": 2, "yield": (5, 20)},
    "Gold": {"value": 300, "difficulty": 3, "yield": (3, 12)},
    "Platinum": {"value": 500, "difficulty": 4, "yield": (2, 8)},
    "Dark Matter Crystal": {"value": 1000, "difficulty": 5, "yield": (1, 4)}
}

mining_upgrades = {
    "Laser Drill": {"owned": False, "cost": 500, "bonus": 0.2},
    "Shield Generator": {"owned": False, "cost": 800, "bonus": 0.3},
    "Cargo Expander": {"owned": False, "cost": 400, "bonus": 0.5}
}

total_mined = 0

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
    },
    "💎 Crystal Asteroid": {
        "description": "Asteroid made of rare crystals!",
        "effect": "mining_bonus",
        "reward": None
    }
}

bounty_targets = [
    {"name": "Red Pirate", "bounty": 500, "level": 1, "health": 3},
    {"name": "Shadow Corsair", "bounty": 1000, "level": 2, "health": 5},
    {"name": "Void Reaver", "bounty": 2000, "level": 3, "health": 7},
    {"name": "Star Eater", "bounty": 5000, "level": 4, "health": 10},
    {"name": "Galactic Menace", "bounty": 10000, "level": 5, "health": 15}
]

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
    "anomaly_hunter": "🔭 Anomaly Hunter - Discover 3 space anomalies",
    "bounty_hunter": "💰 Bounty Hunter - Defeat a bounty target",
    "research_genius": "🧠 Research Genius - Unlock 3 research upgrades",
    "space_whisperer": "🐋 Space Whisperer - Find the space whales",
    "comet_chaser": "☄️ Comet Chaser - Track a comet",
    "galactic_hero": "🦸 Galactic Hero - Reach bounty rank 5",
    "crew_trainer": "🎓 Crew Trainer - Get a crew member to level 5",
    "stock_master": "📈 Stock Master - Make 5000 profit from stock market",
    "mining_baron": "⛏️ Mining Baron - Mine 50 total resources",
    "diplomat": "🤝 Diplomat - Reach 90+ relation with any faction",
    "colonizer": "🏠 Colonizer - Establish your first colony",
    "smuggler": "🕶️ Smuggler - Successfully use the black market 5 times",
    "racing_champion": "🏆 Racing Champion - Win 10 space races",
    "casino_king": "👑 Casino King - Win 10000 credits at the casino",
    "lucky_streak": "🍀 Lucky Streak - Win 5 casino games in a row",
    "challenge_master": "🎯 Challenge Master - Complete 10 daily challenges",
    "pirate_hunter": "🏴‍☠️ Pirate Hunter - Defeat 50 pirate raids",
    "defense_genius": "🛡️ Defense Genius - Own all defense turrets"
}

nebulae = {
    "Orion Nebula": (1340, -220),
    "Eagle Nebula": (7000, 0),
    "Helix Nebula": (695, 280),
    "Crab Nebula": (6500, 190),
    "Tarantula Nebula": (160000, 5000),
    "Horsehead Nebula": (1500, -300),
    "Cat's Eye Nebula": (3000, 400)
}

alien_items = {
    "🌌 dark matter crystal": 500,
    "💫 warp core upgrade": 2000,
    "🔮 quantum shield": 1500,
    "🍕 exotic space pizza": 50,
    "🐉 baby space dragon egg": 3000,
    "📡 anomaly scanner": 800,
    "🔭 research data": 400
}

random_events = [
    {"name": "🌀 WORMHOLE!", "effect": "shortcut", "message": "You found a wormhole! Distance reduced by 40%!", "modifier": 0.6},
    {"name": "🏴‍☠️ SPACE PIRATES!", "effect": "danger", "message": "Space pirates attacked! Lost 200 fuel and 100 credits!", "fuel": -200, "credits": -100},
    {"name": "✨ COSMIC CACHE", "effect": "reward", "message": "Found a floating cargo pod! +300 credits and +150 fuel!", "fuel": 150, "credits": 300},
    {"name": "🌊 SOLAR FLARE", "effect": "danger", "message": "Solar flare damaged shields! Lost 100 fuel!", "fuel": -100},
    {"name": "🤝 FRIENDLY ALIENS", "effect": "reward", "message": "Friendly aliens gave you a gift! +250 credits!", "credits": 250},
    {"name": "📡 MYSTERY SIGNAL", "effect": "anomaly", "message": "Strange signal detected!", "anomaly": True},
    {"name": "☄️ COMET FLYBY", "effect": "comet", "message": "A comet is passing by!", "comet": True}
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

# ============= ANOMALY DISCOVERY =============
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
        
    elif anomaly["effect"] == "gift":
        gain = anomaly["reward"]
        credits_total += gain
        print(f"💰 The anomaly gave you {gain} credits!")
        
    elif anomaly["effect"] == "danger":
        damage = anomaly["damage"]
        if research_upgrades["Shield Tech"]["owned"]:
            damage = int(damage * research_upgrades["Shield Tech"]["value"])
            print(f"🛡️ Shields reduced damage to {damage}!")
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

# ============= BOUNTY HUNTING =============
def bounty_hunting():
    global credits_total, fuel, bounty_hunting_level
    
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
        
        print("⚔️ COMBAT MODE ⚔️")
        player_health = target['health']
        target_health = target['health']
        
        gunner_bonus = 1
        for member in crew_members:
            if member['bonus'] == 'combat_damage':
                gunner_bonus = 1 + (member['level'] * 0.1)
                print(f"🔫 Gunner bonus: +{int((gunner_bonus-1)*100)}% damage!")
        
        while player_health > 0 and target_health > 0:
            print(f"\n❤️ Your health: {player_health} | {target['name']} health: {target_health}")
            action = input("1. Attack | 2. Dodge | 3. Use item: ")
            
            if action == "1":
                damage = int(random.randint(2, 6) * gunner_bonus)
                target_health -= damage
                print(f"⚡ You dealt {damage} damage!")
                
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
            gain_crew_xp(50)
            
            if target["level"] == bounty_hunting_level:
                bounty_hunting_level = min(5, bounty_hunting_level + 1)
                print(f"🏆 Bounty rank increased to {bounty_hunting_level}!")
                
            check_achievement("bounty_hunter")
            if bounty_hunting_level >= 5:
                check_achievement("galactic_hero")
        else:
            print(f"\n💀 Defeated by {target['name']}... Lost 200 credits")
            credits_total = max(0, credits_total - 200)

# ============= RESEARCH LAB =============
def research_lab():
    global research_points, fuel, credits_total
    
    print("\n🧪 RESEARCH LAB 🧪")
    print(f"📚 Research Points: {research_points}")
    print("\nAvailable Upgrades:")
    
    rp_bonus = 1
    for member in crew_members:
        if member['bonus'] == 'rp_bonus':
            rp_bonus = 1 + (member['level'] * 0.05)
            print(f"🔬 Scientist bonus: +{int((rp_bonus-1)*100)}% research efficiency!")
    
    upgrades_list = list(research_upgrades.items())
    for i, (name, data) in enumerate(upgrades_list, 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} RP"
        print(f"{i}. {name} - {status}")
    
    print("\n7. Convert credits to research points (100 credits = 20 RP)")
    print("8. 🎓 Train Crew")
    
    choice = input("\nSelect option (number) or 'quit': ")
    
    if choice == "8":
        train_crew()
    elif choice.isdigit() and 1 <= int(choice) <= len(upgrades_list):
        upgrade_name, upgrade_data = upgrades_list[int(choice)-1]
        if not upgrade_data["owned"]:
            cost = upgrade_data["cost"]
            if research_points >= cost:
                research_points -= cost
                upgrade_data["owned"] = True
                print(f"✨ Unlocked {upgrade_name}! ✨")
                check_achievement("research_genius")
                gain_crew_xp(25)
            else:
                print(f"❌ Need {cost} research points!")
        else:
            print("❌ Already owned!")
            
    elif choice == "7":
        amount = int(input("How many credits to convert? "))
        if amount >= 100:
            rp_gain = (amount // 100) * 20
            credits_total -= amount
            research_points += rp_gain
            print(f"✨ Converted {amount} credits into {rp_gain} research points!")

# ============= COMET TRACKING =============
def track_comet():
    global credits_total, research_points
    
    print("\n☄️ COMET TRACKING SYSTEM ☄️")
    comet = random.choice(comet_names)
    print(f"Tracking comet {comet}...")
    time.sleep(1)
    
    nav_bonus = 1
    for member in crew_members:
        if member['bonus'] == 'distance_bonus':
            nav_bonus = 1 - (member['level'] * 0.02)
            print(f"🧭 Navigator bonus: Easier tracking!")
    
    print("\nAdjust your telescope!")
    target_angle = random.randint(0, 360)
    print(f"Target angle: ???")
    
    guess = int(input("Your guess (0-360): "))
    difference = min(abs(guess - target_angle), 360 - abs(guess - target_angle))
    difference = int(difference * nav_bonus)
    
    if difference < 10:
        reward = 500
        print(f"🎯 PERFECT! You found comet {comet}!")
        print(f"💰 +{reward} credits!")
        credits_total += reward
        research_points += 30
        gain_crew_xp(40)
        check_achievement("comet_chaser")
    elif difference < 30:
        reward = 200
        print(f"👍 Good! You spotted comet {comet}!")
        print(f"💰 +{reward} credits!")
        credits_total += reward
        research_points += 15
        gain_crew_xp(15)
    else:
        print(f"😅 Missed it! The comet was at {target_angle}°")

# ============= ALIEN TRADE =============
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
            gain_crew_xp(10)
            check_achievement("alien_friend")
        else:
            print("❌ Need more credits!")

# ============= EXPLORE NEBULA =============
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
            
            if random.random() < 0.3:
                discover_anomaly()
        else:
            artifact = random.choice(["ancient relic", "crystal shard", "energy core", "star chart"])
            inventory.append(artifact)
            print(f"🔮 Found {artifact}!")
            research_points += 20
            print
