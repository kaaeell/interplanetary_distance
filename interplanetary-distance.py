import math
import random
import time
from datetime import datetime
import os

# the code is getting COOLER nowwwww
# added achievements, fuel system, alien trading, and more!

history = []
total_calculations = 0
highest_distance = 0
missions_completed = 0
fuel = 5000  # Starting fuel in units
credits_total = 1000  # Starting space credits
achievements = []
inventory = []

galaxy_names = ["Milky Way","Andromeda","Sombrero Galaxy","Whirlpool Galaxy","Black Eye Galaxy","Cartwheel Galaxy"]
astronauts = ["Neil","Buzz","Sally","Yuri","Mae","Chris","Valentina"]
spaceships = ["StarRunner","NovaX","Galaxy Rider","Void Explorer","Cosmic Storm","Nebula One"]
space_pets = ["space dog","robot cat","alien hamster","tiny moon dragon"]
badges = ["🌟 rookie pilot badge","🚀 master explorer badge","🪐 galaxy navigator badge","☄️ asteroid survivor badge"]
alien_names = ["Zorg","Xenon","Blip","Nova","Kratos"]
space_foods = ["freeze dried pizza","space tacos","galaxy noodles","moon burgers"]
space_jobs = ["pilot","engineer","galaxy scout","alien translator","space mechanic"]
planet_conditions = ["lava storms detected","ice surface detected","heavy gravity detected","safe landing conditions","radioactive atmosphere detected"]

comet_names = ["Halley","Encke","Hale-Bopp","Swift-Tuttle","Neowise"]
space_jokes = ["Why did the star go to school? To get a little brighter!","What do astronauts use to keep their pants up? An asteroid belt!","Why don't aliens visit our solar system? They read the reviews… only one star!"]
alien_greetings = ["👽 Blip blop!","👾 Greetings Earthling!","🛸 Take me to your leader!","🛸 Beep boop!"]

# NEW: Cool achievements system
achievement_list = {
    "first_step": "🌱 First Step - Complete your first mission",
    "milky_way_tourist": "🌌 Milky Way Tourist - Travel over 2000 million km",
    "fuel_hunter": "⛽ Fuel Hunter - Collect fuel from a nebula",
    "alien_friend": "👽 Alien Friend - Successfully trade with aliens",
    "millionaire": "💰 Space Millionaire - Earn 10,000 credits",
    "speed_demon": "⚡ Speed Demon - Complete a mission in under 30 seconds",
    "badge_collector": "🎖️ Badge Collector - Earn 5 different badges",
    "pet_lover": "🐾 Pet Lover - Adopt a space pet",
    "galaxy_legend": "⭐ Galaxy Legend - Complete 50 missions"
}

# NEW: Nebula locations for fuel collection
nebulae = {
    "Orion Nebula": (1340, -220),
    "Eagle Nebula": (7000, 0),
    "Helix Nebula": (695, 280),
    "Crab Nebula": (6500, 190),
    "Tarantula Nebula": (160000, 5000)
}

# NEW: Alien trading items
alien_items = {
    "🌌 dark matter crystal": 500,
    "💫 warp core upgrade": 2000,
    "🔮 quantum shield": 1500,
    "🍕 exotic space pizza": 50,
    "🐉 baby space dragon egg": 3000
}

def calculate_distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def get_coordinates(name):
    while True:
        try:
            print(f"\nEnter coordinates for {name} (in million km)")
            x = float(input("x: "))
            y = float(input("y: "))
            return (x,y)
        except ValueError:
            print("invalid input")

def choose_planets():
    planets = {
        1: ("Earth",(0,0)),2: ("Mars",(225,0)),3: ("Venus",(108,0)),4: ("Jupiter",(778,0)),
        5: ("Saturn",(1427,0)),6: ("Uranus",(2871,0)),7: ("Neptune",(4495,0)),8: ("Mercury",(58,0)),
        9: ("Pluto",(5906,0)),10: ("Moon",(1,0))
    }
    print("\n📋 Available planets:")
    for num,(name,_) in planets.items():
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
    p1_name,p1 = pick("Choose planet 1: ")
    p2_name,p2 = pick("Choose planet 2: ")
    return p1_name,p1,p2_name,p2

# NEW: Fuel check before mission
def check_fuel(distance):
    global fuel
    fuel_needed = distance * 0.5  # 0.5 fuel units per million km
    if fuel < fuel_needed:
        print(f"\n⚠️ INSUFFICIENT FUEL! Need {fuel_needed:.1f} units, have {fuel:.1f}")
        print("🎲 Attempting emergency fuel collection...")
        collect_emergency_fuel()
        return check_fuel(distance)  # Recursive check after collection
    else:
        fuel -= fuel_needed
        print(f"⛽ Fuel used: {fuel_needed:.1f} units | Remaining: {fuel:.1f}")
        return True

# NEW: Emergency fuel collection mini-game
def collect_emergency_fuel():
    global fuel, credits_total
    print("\n🔄 EMERGENCY FUEL COLLECTION MODE 🔄")
    print("You have 3 options:")
    print("1. 🛸 Mine nearby asteroid (risky but free)")
    print("2. 💰 Buy fuel from space station (costs credits)")
    print("3. 🎲 Try your luck at space casino (gamble!)")
    
    choice = input("Choose: ")
    
    if choice == "1":
        success = random.random() < 0.6
        if success:
            gained = random.randint(200, 800)
            fuel += gained
            print(f"✅ Asteroid mining successful! +{gained} fuel")
        else:
            damage = random.randint(50, 200)
            fuel = max(0, fuel - damage)
            print(f"💥 Asteroid mining failed! Lost {damage} fuel")
            
    elif choice == "2":
        cost_per_unit = 2
        print(f"💰 Fuel price: {cost_per_unit} credits per unit")
        amount = int(input("How much fuel to buy? "))
        total_cost = amount * cost_per_unit
        if credits_total >= total_cost:
            credits_total -= total_cost
            fuel += amount
            print(f"✅ Bought {amount} fuel! Remaining credits: {credits_total}")
        else:
            print("❌ Not enough credits!")
            collect_emergency_fuel()
            
    elif choice == "3":
        bet = int(input("How many credits to gamble? "))
        if bet > credits_total:
            print("Not enough credits!")
            return
        roll = random.randint(1, 100)
        if roll > 70:
            winnings = bet * random.uniform(1.5, 3)
            credits_total += winnings
            fuel += random.randint(100, 400)
            print(f"🎉 YOU WIN! +{winnings:.0f} credits and +{fuel} fuel!")
        else:
            credits_total -= bet
            print(f"💀 You lost {bet} credits... Better luck next time!")

# NEW: Alien trading system
def alien_trade():
    global credits_total, inventory
    print("\n🛸 ALIEN TRADING POST 🛸")
    print(f"💰 Your credits: {credits_total}")
    print("\nAvailable items:")
    
    items_list = list(alien_items.items())
    for i, (item, price) in enumerate(items_list, 1):
        print(f"{i}. {item} - {price} credits")
    
    choice = input("Buy item (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(items_list):
        item, price = items_list[int(choice)-1]
        if credits_total >= price:
            credits_total -= price
            inventory.append(item)
            print(f"✨ You bought {item}! ✨")
            check_achievement("alien_friend")
        else:
            print("❌ Not enough credits!")
    elif choice.lower() == 'quit':
        print("👋 Safe travels!")

# NEW: Nebula exploration for fuel
def explore_nebula():
    global fuel, achievements
    print("\n🌌 NEBULA EXPLORATION MODE 🌌")
    print("Nearby nebulae:")
    neb_list = list(nebulae.items())
    for i, (name, coords) in enumerate(neb_list, 1):
        print(f"{i}. {name} at {coords}")
    
    choice = input("Explore nebula (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(neb_list):
        neb_name, coords = neb_list[int(choice)-1]
        print(f"\n🚀 Warping to {neb_name}...")
        time.sleep(1)
        
        # Calculate distance from current position (assuming origin for simplicity)
        distance = calculate_distance((0,0), coords)
        print(f"Distance traveled: {distance:.0f} million km")
        
        # Random nebula event
        event_roll = random.random()
        if event_roll < 0.7:
            fuel_gained = random.randint(300, 1500)
            fuel += fuel_gained
            print(f"⛽ Collected {fuel_gained} fuel from the nebula!")
            check_achievement("fuel_hunter")
        elif event_roll < 0.9:
            artifact = random.choice(["ancient alien artifact", "crystal shard", "energy core"])
            inventory.append(artifact)
            print(f"🔮 Found {artifact}! Added to inventory.")
        else:
            damage = random.randint(100, 400)
            fuel = max(0, fuel - damage)
            print(f"⚠️ Nebula storm damaged your ship! Lost {damage} fuel")

# NEW: Achievement checker
def check_achievement(achievement_key):
    global achievements
    achievement_name = achievement_list.get(achievement_key)
    if achievement_name and achievement_key not in achievements:
        achievements.append(achievement_key)
        print(f"\n🏆 ACHIEVEMENT UNLOCKED: {achievement_name} 🏆")

# NEW: Daily bonus system
def daily_bonus():
    global credits_total, fuel
    print("\n🎁 DAILY LOGIN BONUS 🎁")
    bonus_credits = random.randint(200, 800)
    bonus_fuel = random.randint(100, 300)
    credits_total += bonus_credits
    fuel += bonus_fuel
    print(f"✨ +{bonus_credits} credits")
    print(f"✨ +{bonus_fuel} fuel")
    print("Thanks for playing space commander!")

# NEW: Space race challenge
def space_race():
    global credits_total, fuel
    print("\n🏁 SPACE RACE CHALLENGE 🏁")
    print("Race from Earth to Mars!")
    distance = calculate_distance((0,0), (225,0))
    print(f"Race distance: {distance} million km")
    
    start_time = time.time()
    input("Press ENTER when ready to start the race!")
    print("3... 2... 1... GO! 🚀")
    
    # Simple reaction game
    reaction_time = random.uniform(0.5, 2.0)
    time.sleep(reaction_time)
    print("🟢 GO NOW!")
    start_race = time.time()
    input()
    end_time = time.time()
    
    race_time = end_time - start_race
    print(f"Your time: {race_time:.2f} seconds")
    
    if race_time < 0.5:
        winnings = 1000
        print(f"🏆 AMAZING! You win {winnings} credits!")
        credits_total += winnings
        check_achievement("speed_demon")
    elif race_time < 1.0:
        winnings = 500
        print(f"👍 Good job! You win {winnings} credits!")
        credits_total += winnings
    else:
        print("😅 Keep practicing commander!")

def show_fun_fact():
    facts = ["Venus spins backwards","Mars sunsets are blue","Saturn could float in water","Jupiter is insanely huge","Neptune has crazy strong winds","A day on Venus is longer than a year there"]
    print(f"\n📚 fun fact: {random.choice(facts)}")

def show_space_event():
    events = ["☄️ comet detected nearby","🌠 meteor shower active","🛰️ signal received from deep space","👽 aliens definitely watching","🪐 strange rings detected nearby"]
    print(f"✨ {random.choice(events)}")

def random_space_weather():
    weather = ["☀️ solar activity calm today","🌌 radiation levels normal","☄️ asteroid traffic kinda high rn","🛰️ satellites working fine","⚡ solar storm warning active"]
    print(f"\n🌦️ space weather: {random.choice(weather)}")

def mission_status():
    missions = ["✅ mission completed successfully","🚀 navigation systems online","⚠️ fuel levels questionable","🌌 deep space systems stable"]
    print(f"📡 {random.choice(missions)}")

def detect_black_hole():
    chance = random.randint(1,12)
    if chance==1:
        print("🕳️ ⚠️ BLACK HOLE DETECTED NEARBY! EVASIVE MANEUVERS! ⚠️")
        global fuel
        fuel -= random.randint(50, 200)
        print(f"⛽ Evasive maneuvers cost {min(50, fuel)} fuel!")
    else:
        print("✅ no black holes nearby")

def oxygen_level():
    oxygen = random.randint(70,100)
    print(f"🫁 oxygen levels: {oxygen}%")

def random_rank(distance):
    if distance>5000: print("🏆 rank: intergalactic traveler ✨")
    elif distance>3000: print("🏆 rank: galaxy traveler 🌌")
    elif distance>1000: print("🏆 rank: space explorer 🚀")
    elif distance>300: print("🏆 rank: orbit runner 🏃")
    else: print("🏆 rank: moon walker 🌙")

def random_galaxy(): print(f"🌌 nearby galaxy detected: {random.choice(galaxy_names)}")
def random_astronaut(): print(f"👨‍🚀 astronaut online: {random.choice(astronauts)}")
def random_spaceship(): print(f"🛸 active spaceship: {random.choice(spaceships)}")

def distance_category(distance):
    if distance<100: print("📍 category: super short trip")
    elif distance<1000: print("📍 category: medium trip")
    elif distance<3000: print("📍 category: long trip")
    else: print("📍 category: extreme space travel")

def random_signal():
    signals = ["📡 strange radio signal detected","📡 signal strength stable","📡 communication delay increased","📡 deep space signal lost briefly"]
    print(random.choice(signals))

def moon_phase():
    phases = ["🌕 full moon tonight","🌗 half moon detected","🌑 new moon phase active","🌙 crescent moon visible"]
    print(random.choice(phases))

def crew_mood():
    moods = ["😄 crew feeling great","😴 crew tired but working","🤖 robots handling repairs","🧑‍🚀 crew excited for mission"]
    print(random.choice(moods))

def temperature_check(): print(f"🌡️ nearby temperature: {random.randint(-150,120)}°C")
def danger_level(): print(random.choice(["🟢 danger level: low","🟡 danger level: medium","🟠 danger level: high","🔴 danger level: critical"]))
def daily_space_tip(): print(random.choice(["💡 tip: always double check coordinates","💡 tip: keep fuel above 30%","💡 tip: avoid black holes if possible","💡 tip: deep space signals can be delayed","💡 tip: nebulae are great for fuel collection"]))
def random_space_pet(): 
    pet = random.choice(space_pets)
    print(f"🐾 companion detected: {pet}")
    if random.random() < 0.1:  # 10% chance to adopt
        inventory.append(pet)
        print(f"🎉 {pet} joined your crew!")
        check_achievement("pet_lover")
def random_badge(): 
    badge = random.choice(badges)
    print(f"🎖️ badge earned: {badge}")
    if len([b for b in achievements if "badge" in b]) >= 5:
        check_achievement("badge_collector")
def signal_strength(): print(f"📶 signal strength: {random.randint(40,100)}%")
def credits_display(): print(f"💰 space credits: {credits_total}")
def asteroid_scan(): 
    asteroids = random.randint(0,12)
    print(f"🪨 asteroids nearby: {asteroids}")
    if asteroids > 8:
        print("⚠️ Heavy asteroid field! Be careful!")
def alien_encounter(): 
    if random.randint(1,5)==1:
        alien = random.choice(alien_names)
        print(f"👽 ALIEN ENCOUNTER with {alien}!")
        alien_trade()
    else:
        print("👽 no aliens contacted today")
def space_food(): print(f"🍔 crew meal today: {random.choice(space_foods)}")
def engine_status(): print(random.choice(["🛠️ engines running perfectly","⚠️ engine heat slightly high","🚀 boosters ready","🔧 engine maintenance recommended"]))
def warp_drive(): print(f"💫 warp drive power: {random.randint(10,100)}%")
def random_space_job(): print(f"🧑‍🚀 current crew role: {random.choice(space_jobs)}")
def planet_condition(): print(f"🪐 planet scan: {random.choice(planet_conditions)}")
def shield_status(): print(f"🛡️ shield power: {random.randint(20,100)}%")
def laser_power(): print(f"🔫 laser system power: {random.randint(10,100)}%")
def gravity_level(): print(f"🌍 gravity level: {round(random.uniform(0.2,5.0),2)}G")

def show_all_fluff(distance):
    """Show all the fun random space info after a calculation"""
    print("\n" + "="*50)
    random_space_weather()
    show_space_event()
    random_galaxy()
    random_astronaut()
    random_spaceship()
    distance_category(distance)
    random_rank(distance)
    random_signal()
    moon_phase()
    crew_mood()
    temperature_check()
    danger_level()
    daily_space_tip()
    random_space_pet()
    random_badge()
    signal_strength()
    credits_display()
    asteroid_scan()
    alien_encounter()
    space_food()
    engine_status()
    warp_drive()
    random_space_job()
    planet_condition()
    shield_status()
    laser_power()
    gravity_level()
    detect_black_hole()
    oxygen_level()
    mission_status()
    show_fun_fact()
    print("="*50)

def show_stats_dashboard():
    """NEW: Cool stats dashboard"""
    print("\n" + "="*50)
    print("🚀 SPACE COMMANDER STATS DASHBOARD 🚀")
    print("="*50)
    print(f"📊 Total calculations: {total_calculations}")
    print(f"📜 Saved history count: {len(history)}")
    print(f"🏆 Highest distance: {highest_distance:.2f} million km")
    print(f"🚀 Missions completed: {missions_completed}")
    print(f"⛽ Current fuel: {fuel:.1f} units")
    print(f"💰 Total credits: {credits_total}")
    print(f"🎖️ Achievements: {len(achievements)}/{len(achievement_list)}")
    print(f"🎒 Inventory items: {len(inventory)}")
    
    if inventory:
        print("\n🎒 INVENTORY:")
        for item in inventory[-5:]:  # Show last 5 items
            print(f"  • {item}")
    
    if achievements:
        print("\n🏆 UNLOCKED ACHIEVEMENTS:")
        for ach in achievements[-5:]:
            print(f"  • {achievement_list[ach]}")
    
    print("="*50)

def main():
    global total_calculations, highest_distance, missions_completed, fuel, credits_total
    
    print("\n" + "🌌" * 20)
    print("🚀 SPACE DISTANCE CALCULATOR - ULTIMATE EDITION 🚀")
    print("🌌" * 20)
    print(random.choice(["space calculator v13 ready","doing questionable space math","probably accurate enough","welcome back commander","time to explore the cosmos!"]))
    
    today = datetime.now()
    print(f"📅 date: {today.strftime('%Y-%m-%d')} 🕒 time: {today.strftime('%H:%M:%S')}")
    
    # Daily bonus on first run
    daily_bonus()
    
    while True:
        print("\n" + "="*40)
        print("MAIN MENU")
        print("="*40)
        print("1️⃣  Calculate planet distance")
        print("2️⃣  Calculate custom coordinates")
        print("3️⃣  View mission history")
        print("4️⃣  View stats dashboard")
        print("5️⃣  Clear history")
        print("6️⃣  🌌 Explore Nebula (collect fuel)")
        print("7️⃣  🛸 Alien Trading Post")
        print("8️⃣  🏁 Space Race Challenge")
        print("9️⃣  🎒 View inventory")
        print("0️⃣  Exit game")
        
        mode = input("\nSelect option: ").strip()
        
        if mode == "3":
            print("\n📜 MISSION HISTORY:" if history else "📜 No history yet")
            for item in history[-10:]:  # Show last 10 entries
                print(f"  {item}")
            if len(history) > 10:
                print(f"  ... and {len(history)-10} more missions")
            continue
            
        if mode == "4":
            show_stats_dashboard()
            continue
            
        if mode == "5":
            history.clear()
            print("🧹 History cleared!")
            continue
            
        if mode == "6":
            explore_nebula()
            continue
            
        if mode == "7":
            alien_trade()
            continue
            
        if mode == "8":
            space_race()
            continue
            
        if mode == "9":
            print("\n🎒 YOUR INVENTORY 🎒")
            if inventory:
                for item in inventory:
                    print(f"  • {item}")
            else:
                print("  Empty! Visit alien traders or explore nebulae!")
            continue
            
        if mode == "0":
            print("\n👋 Thanks for playing Space Commander!")
            print(f"Final stats: {missions_completed} missions | {len(achievements)} achievements | {credits_total} credits")
            print("🖖 Live long and prosper!")
            break
            
        if mode == "1":
            # Planet mode with fuel check
            p1_name, p1, p2_name, p2 = choose_planets()
            distance = calculate_distance(p1, p2)
            
            # Check if we have enough fuel
            if not check_fuel(distance):
                print("❌ Mission aborted due to fuel shortage!")
                continue
            
        elif mode == "2":
            # Custom coordinates mode
            print("\n✨ CUSTOM LOCATION MODE ✨")
            p1_name = input("Name of starting location: ") or "Start"
            p2_name = input("Name of destination: ") or "Destination"
            p1 = get_coordinates(p1_name)
            p2 = get_coordinates(p2_name)
            distance = calculate_distance(p1, p2)
            
            if not check_fuel(distance):
                print("❌ Mission aborted due to fuel shortage!")
                continue
            
        else:
            print("❌ Invalid option. Choose 0-9")
            continue
            
        # Process the calculation
        total_calculations += 1
        missions_completed += 1
        
        # Add credits for completing mission
        credit_reward = int(distance * 0.5) + random.randint(50, 200)
        credits_total += credit_reward
        print(f"💰 Mission reward: {credit_reward} credits!")
        
        if distance > highest_distance:
            highest_distance = distance
            print("\n🎉 NEW RECORD DISTANCE! 🎉")
            if distance > 2000:
                check_achievement("milky_way_tourist")
        
        print(f"\n{'='*50}")
        print(f"📍 FROM: {p1_name} {p1}")
        print(f"📍 TO: {p2_name} {p2}")
        print(f"📏 DISTANCE: {distance:.2f} million km")
        print(f"{'='*50}")
        
        # Store in history
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = f"[{timestamp}] {p1_name} → {p2_name}: {distance:.2f} million km"
        history.append(history_entry)
        
        # Show all the fun space info
        show_all_fluff(distance)
        
        # Special milestone messages
        if missions_completed == 1:
            check_achievement("first_step")
        if missions_completed % 10 == 0:
            print(f"\n🎉 MISSION MILESTONE! {missions_completed} missions completed! 🎉")
            print(random.choice(alien_greetings))
            print(random.choice(space_jokes))
        
        if credits_total >= 10000:
            check_achievement("millionaire")
        
        if missions_completed >= 50:
            check_achievement("galaxy_legend")

if __name__ == "__main__":
    main()
