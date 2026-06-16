import math
import random
import time
from datetime import datetime
import json
import os

# SPACE DISTANCE CALCULATOR - ULTIMATE EDITION v3.2
# New today: Space anomalies, research system, bounty hunting, CREW SKILL SYSTEM, 
# SPACE STOCK MARKET, SPACE MINING, DIPLOMATIC RELATIONS, PLANETARY COLONIZATION, 
# BLACK MARKET, SPACE RACING LEAGUE, and SPACE CASINO!


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

# ============= NEW: SPACE CASINO =============
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
    "lucky_streak": "🍀 Lucky Streak - Win 5 casino games in a row"
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

# ============= NEW: SPACE CASINO =============
def space_casino():
    global credits_total, crew_morale
    
    print("\n🎰 SPACE CASINO 🎰")
    print("=" * 50)
    print(f"💰 Your Credits: {credits_total}")
    print(f"🎯 Biggest Win: {casino_stats['biggest_win']} credits")
    print("\nAvailable Games:")
    
    games_list = list(casino_games.items())
    for i, (game, data) in enumerate(games_list, 1):
        print(f"{i}. {game}")
        print(f"   Min Bet: {data['min_bet']} | Max Bet: {data['max_bet']} | Jackpot: {data['jackpot']}")
    
    print("\n5. View Casino Stats")
    print("6. Back")
    
    choice = input("\nChoose game: ")
    
    if choice == "5":
        view_casino_stats()
    elif choice.isdigit() and 1 <= int(choice) <= len(games_list):
        game_name, game_data = games_list[int(choice)-1]
        play_casino_game(game_name, game_data)

def play_casino_game(game_name, game_data):
    global credits_total, crew_morale, casino_stats
    
    print(f"\n🎮 PLAYING: {game_name} 🎮")
    print(f"💰 Your Credits: {credits_total}")
    
    bet = int(input(f"Enter bet ({game_data['min_bet']}-{game_data['max_bet']}): "))
    
    if bet < game_data['min_bet'] or bet > game_data['max_bet']:
        print("❌ Invalid bet amount!")
        return
    
    if bet > credits_total:
        print("❌ Not enough credits!")
        return
    
    credits_total -= bet
    casino_stats['total_bet'] += bet
    
    print("\n🔄 Spinning...")
    time.sleep(1.5)
    
    # Different game mechanics
    if game_name == "Cosmic Slots":
        result = play_slots(bet, game_data)
    elif game_name == "Alien Poker":
        result = play_poker(bet, game_data)
    elif game_name == "Roulette":
        result = play_roulette(bet, game_data)
    elif game_name == "Black Hole Blackjack":
        result = play_blackjack(bet, game_data)
    
    if result > 0:
        credits_total += result
        casino_stats['total_won'] += result
        if result > casino_stats['biggest_win']:
            casino_stats['biggest_win'] = result
            print(f"🏆 NEW BIGGEST WIN! 🏆")
        
        # Check achievements
        if casino_stats['total_won'] >= 10000:
            check_achievement("casino_king")
        
        # Check lucky streak (simplified)
        if casino_stats['games_played'] > 0 and casino_stats['games_played'] % 5 == 0:
            check_achievement("lucky_streak")
        
        # Crew morale boost from winning
        morale_gain = random.randint(5, 15)
        crew_morale = min(100, crew_morale + morale_gain)
        print(f"😊 Crew morale +{morale_gain}! (Now: {crew_morale}%)")
    else:
        # Crew morale drop from losing
        morale_loss = random.randint(5, 10)
        crew_morale = max(0, crew_morale - morale_loss)
        print(f"😞 Crew morale -{morale_loss}! (Now: {crew_morale}%)")
    
    casino_stats['games_played'] += 1
    gain_crew_xp(5)

def play_slots(bet, game_data):
    print("🎰 SPINNING SLOTS...")
    
    symbols = ["🍒", "⭐", "🔔", "💎", "7️⃣", "🎰"]
    results = [random.choice(symbols) for _ in range(3)]
    
    print(f"Results: {' '.join(results)}")
    
    if results[0] == results[1] == results[2]:
        if results[0] == "7️⃣":
            winnings = bet * 50
            print(f"🎉 JACKPOT! Won {winnings} credits!")
            return winnings
        elif results[0] == "💎":
            winnings = bet * 20
            print(f"💰 Diamond triple! Won {winnings} credits!")
            return winnings
        else:
            winnings = bet * 5
            print(f"💰 Triple match! Won {winnings} credits!")
            return winnings
    elif results[0] == results[1] or results[1] == results[2] or results[0] == results[2]:
        winnings = bet * 2
        print(f"💰 Pair! Won {winnings} credits!")
        return winnings
    else:
        print("❌ No match! You lose!")
        return 0

def play_poker(bet, game_data):
    print("♠️ ALIEN POKER ♠️")
    
    # Simple poker simulation
    player_hand = random.randint(1, 13) + random.randint(1, 13) / 100
    dealer_hand = random.randint(1, 13) + random.randint(1, 13) / 100
    
    print(f"Your hand: {int(player_hand)}")
    print(f"Dealer hand: {int(dealer_hand)}")
    
    if player_hand > dealer_hand:
        winnings = bet * 2
        print(f"🎉 You win! Won {winnings} credits!")
        return winnings
    elif player_hand == dealer_hand:
        winnings = bet
        print(f"🤝 Push! Bet returned!")
        return winnings
    else:
        print("❌ You lose!")
        return 0

def play_roulette(bet, game_data):
    print("🎡 ROULETTE 🎡")
    
    print("\nBet on:")
    print("1. Red")
    print("2. Black")
    print("3. Green (0)")
    print("4. Even")
    print("5. Odd")
    
    choice = input("Choose your bet type: ")
    number = random.randint(0, 36)
    
    print(f"🎯 Ball landed on: {number}")
    
    if choice == "1":  # Red
        red_numbers = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        if number in red_numbers:
            winnings = bet * 2
            print(f"🎉 Red wins! Won {winnings} credits!")
            return winnings
        else:
            print("❌ Not red! You lose!")
            return 0
    elif choice == "2":  # Black
        black_numbers = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        if number in black_numbers:
            winnings = bet * 2
            print(f"🎉 Black wins! Won {winnings} credits!")
            return winnings
        else:
            print("❌ Not black! You lose!")
            return 0
    elif choice == "3":  # Green
        if number == 0:
            winnings = bet * 35
            print(f"🎉 GREEN! Won {winnings} credits!")
            return winnings
        else:
            print("❌ Not green! You lose!")
            return 0
    elif choice == "4":  # Even
        if number % 2 == 0 and number != 0:
            winnings = bet * 2
            print(f"🎉 Even wins! Won {winnings} credits!")
            return winnings
        else:
            print("❌ Not even! You lose!")
            return 0
    elif choice == "5":  # Odd
        if number % 2 != 0:
            winnings = bet * 2
            print(f"🎉 Odd wins! Won {winnings} credits!")
            return winnings
        else:
            print("❌ Not odd! You lose!")
            return 0
    else:
        print("Invalid choice!")
        return 0

def play_blackjack(bet, game_data):
    print("🃏 BLACK HOLE BLACKJACK 🃏")
    
    # Simple blackjack simulation
    player_total = random.randint(15, 21)
    dealer_total = random.randint(14, 20)
    
    print(f"Your total: {player_total}")
    print(f"Dealer total: {dealer_total}")
    
    if player_total > 21:
        print("💀 Bust! You lose!")
        return 0
    elif dealer_total > 21:
        winnings = bet * 2
        print(f"🎉 Dealer bust! Won {winnings} credits!")
        return winnings
    elif player_total > dealer_total:
        winnings = bet * 2
        print(f"🎉 You win! Won {winnings} credits!")
        return winnings
    elif player_total == dealer_total:
        winnings = bet
        print(f"🤝 Push! Bet returned!")
        return winnings
    else:
        print("❌ You lose!")
        return 0

def view_casino_stats():
    print("\n🎰 CASINO STATISTICS 🎰")
    print("=" * 40)
    print(f"Games Played: {casino_stats['games_played']}")
    print(f"Total Bet: {casino_stats['total_bet']} credits")
    print(f"Total Won: {casino_stats['total_won']} credits")
    print(f"Net Profit: {casino_stats['total_won'] - casino_stats['total_bet']} credits")
    print(f"Biggest Win: {casino_stats['biggest_win']} credits")
    if casino_stats['games_played'] > 0:
        win_rate = (casino_stats['total_won'] / casino_stats['total_bet']) * 100
        print(f"Win Rate: {win_rate:.1f}%")

# ============= SPACE RACING LEAGUE =============
def space_racing():
    global credits_total, fuel, crew_morale
    
    print("\n🏁 SPACE RACING LEAGUE 🏁")
    print("=" * 50)
    print(f"🏆 Races Entered: {racing_stats['races_entered']}")
    print(f"🏆 Races Won: {racing_stats['races_won']}")
    print(f"⭐ Best Time: {racing_stats['best_time']:.2f} seconds")
    print(f"💰 Total Winnings: {racing_stats['total_winnings']} credits")
    
    print("\nAvailable Tracks:")
    for i, track in enumerate(race_tracks, 1):
        record_emoji = "🏆" if racing_stats['best_time'] < track['record'] else "📝"
        print(f"{i}. {track['name']} - Difficulty: {'⭐'*track['difficulty']}")
        print(f"   Prize: {track['prize']} credits | Record: {track['record']:.1f}s {record_emoji}")
    
    print("\n6. Buy Racing Upgrades")
    print("7. View Racing Stats")
    print("8. Back")
    
    choice = input("\nChoose option: ")
    
    if choice == "6":
        buy_racing_upgrades()
    elif choice == "7":
        view_racing_stats()
    elif choice.isdigit() and 1 <= int(choice) <= len(race_tracks):
        race(int(choice)-1)

def race(track_index):
    global credits_total, fuel, crew_morale, racing_stats
    
    track = race_tracks[track_index]
    
    print(f"\n🏁 STARTING RACE: {track['name']} 🏁")
    print("=" * 40)
    
    ship_bonus = 1.0
    for member in crew_members:
        if member['bonus'] == 'distance_bonus':
            ship_bonus += member['level'] * 0.05
    
    for upgrade, data in racing_upgrades.items():
        if data["owned"]:
            ship_bonus += data["bonus"]
            print(f"✅ {upgrade} active! +{int(data['bonus']*100)}% speed")
    
    morale_bonus = 1 + (crew_morale / 200)
    
    print("\nPress ENTER as fast as you can when you see 'GO!'")
    input("Ready? Press ENTER...")
    
    countdown = random.uniform(1, 4)
    time.sleep(countdown)
    print("🏁 GO! 🏁")
    
    start_time = time.time()
    input()
    reaction_time = time.time() - start_time
    
    base_time = track['record'] * (0.8 + random.random() * 0.4)
    reaction_penalty = reaction_time * 5
    difficulty_penalty = track['difficulty'] * 3
    
    race_time = base_time + reaction_penalty + difficulty_penalty
    race_time = race_time / (ship_bonus * morale_bonus)
    
    print(f"\n⏱️ Your reaction time: {reaction_time:.3f}s")
    print(f"⏱️ Total race time: {race_time:.2f}s")
    print(f"🏆 Track record: {track['record']:.2f}s")
    
    if race_time < track['record']:
        print("\n🎉 NEW TRACK RECORD! 🎉")
        track['record'] = race_time
        if race_time < racing_stats['best_time']:
            racing_stats['best_time'] = race_time
        racing_stats['races_won'] += 1
        prize_multiplier = 2
        print(f"🌟 Bonus for beating record! x{prize_multiplier}")
    elif race_time < track['record'] * 1.2:
        print("\n✅ You won the race!")
        prize_multiplier = 1
        racing_stats['races_won'] += 1
    elif race_time < track['record'] * 1.5:
        print("\n🥈 You placed 2nd!")
        prize_multiplier = 0.5
    else:
        print("\n😔 You lost the race...")
        prize_multiplier = 0
    
    if prize_multiplier > 0:
        winnings = int(track['prize'] * prize_multiplier)
        credits_total += winnings
        racing_stats['total_winnings'] += winnings
        print(f"💰 Won {winnings} credits!")
        
        fuel_cost = track['difficulty'] * 30
        fuel = max(0, fuel - fuel_cost)
        print(f"⛽ Race consumed {fuel_cost} fuel")
        
        gain_crew_xp(15 * track['difficulty'])
        
        if racing_stats['races_won'] >= 10:
            check_achievement("racing_champion")
    else:
        repair_cost = track['difficulty'] * 50
        credits_total = max(0, credits_total - repair_cost)
        print(f"🔧 Repairs cost {repair_cost} credits")
    
    racing_stats['races_entered'] += 1
    update_crew_morale(0, prize_multiplier > 0)

def buy_racing_upgrades():
    global credits_total
    
    print("\n🔧 RACING UPGRADE SHOP 🔧")
    print(f"💰 Credits: {credits_total}")
    print("\nAvailable upgrades:")
    
    upgrades_list = list(racing_upgrades.items())
    for i, (name, data) in enumerate(upgrades_list, 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} credits"
        print(f"{i}. {name} - {status} (+{int(data['bonus']*100)}% speed)")
    
    choice = input("\nSelect upgrade (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(upgrades_list):
        upgrade_name, upgrade_data = upgrades_list[int(choice)-1]
        if not upgrade_data["owned"]:
            if credits_total >= upgrade_data["cost"]:
                credits_total -= upgrade_data["cost"]
                upgrade_data["owned"] = True
                print(f"✨ Purchased {upgrade_name}! ✨")
                print(f"⚡ Speed increased by {int(upgrade_data['bonus']*100)}%")
            else:
                print(f"❌ Need {upgrade_data['cost']} credits!")
        else:
            print("❌ Already owned!")

def view_racing_stats():
    print("\n🏆 RACING STATISTICS 🏆")
    print("=" * 40)
    print(f"Races Entered: {racing_stats['races_entered']}")
    print(f"Races Won: {racing_stats['races_won']}")
    print(f"Win Rate: {(racing_stats['races_won']/racing_stats['races_entered']*100) if racing_stats['races_entered'] > 0 else 0:.1f}%")
    print(f"Best Time: {racing_stats['best_time']:.2f}s")
    print(f"Total Winnings: {racing_stats['total_winnings']} credits")
    
    print("\n🔧 Owned Upgrades:")
    upgrades_owned = [name for name, data in racing_upgrades.items() if data["owned"]]
    if upgrades_owned:
        for upgrade in upgrades_owned:
            print(f"  ✅ {upgrade}")
    else:
        print("  None")
    
