#BR 2nd character creator
import random
from helper import *
from classes import *
from faker import Faker
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
fake = Faker()

characters = {}
for i in csv_to_dict("individual_projects/character_creator/docs/characters.csv"):
    characters[i["name"]] = Character(i["name"], i["race"], i["class"], i["skill"], i["strength"], i["intelligence"], i["wisdom"], i["charisma"], i["dexterity"], i["constitution"], i["inventory"], i["inv_weight"], i["backstory"], i["description"])

races = (
   {
       "name": "Elf",
       "strength_modifier": 1,
       "intelligence_modifier": 3,
       "wisdom_modifier": 2,
       "charisma_modifier": 2,
       "dexterity_modifier": 2,
       "constitution_modifier": 0,
   },
   {
       "name": "Dwarf",
       "strength_modifier": 3,
       "intelligence_modifier": -1,
       "wisdom_modifier": 2,
       "charisma_modifier": -1,
       "dexterity_modifier": 0,
       "constitution_modifier": 1,
   },
   {
       "name": "Orc",
       "strength_modifier": 3,
       "intelligence_modifier": -2,
       "wisdom_modifier": 1,
       "charisma_modifier": -2,
       "dexterity_modifier": 2,
       "constitution_modifier": 1,
   },
   {
       "name": "Goblin",
       "strength_modifier": 0,
       "intelligence_modifier": 1,
       "wisdom_modifier": 1,
       "charisma_modifier": -1,
       "dexterity_modifier": 2,
       "constitution_modifier": 2,
   },
   {
       "name": "Halfling",
       "strength_modifier": 0,
       "intelligence_modifier": 1,
       "wisdom_modifier": 0,
       "charisma_modifier": 0,
       "dexterity_modifier": 2,
       "constitution_modifier": 1,
   },
)


classes = (
   {
   "name":"Paladin",
   "strength_modifier": 2,
   "intelligence_modifier": 1,
   "wisdom_modifier": 2,
   "charisma_modifier": 2,
   "dexterity_modifier": 1,
   "constitution_modifier": 2,
}, {
   "name":"Rogue",
   "strength_modifier": 1,
   "intelligence_modifier": 2,
   "wisdom_modifier": 1,
   "charisma_modifier": 2,
   "dexterity_modifier": 4,
   "constitution_modifier": 1,
}, {
   "name":"Monk",
   "strength_modifier": 1,
   "intelligence_modifier": 2,
   "wisdom_modifier": 2,
   "charisma_modifier": 1,
   "dexterity_modifier": 2,
   "constitution_modifier": 1,
},{
   "name":"Mage",
   "strength_modifier": -1,
   "intelligence_modifier": 4,
   "wisdom_modifier": 2,
   "charisma_modifier": 1,
   "dexterity_modifier": 0,
   "constitution_modifier": 0,
}, {
   "name":"Hunter",
   "strength_modifier": 2,
   "intelligence_modifier": 1,
   "wisdom_modifier": 2,
   "charisma_modifier": 0,
   "dexterity_modifier": 2,
   "constitution_modifier": 2,
}, {
   "name":"Warrior",
   "strength_modifier": 4,
   "intelligence_modifier": 1,
   "wisdom_modifier": 2,
   "charisma_modifier": 1,
   "dexterity_modifier": 2,
   "constitution_modifier": 3,
}, {
   "name":"Druid",
   "strength_modifier": 2,
   "intelligence_modifier": 3,
   "wisdom_modifier": 4,
   "charisma_modifier": 1,
   "dexterity_modifier": 2,
   "constitution_modifier": 3,
})

#Create a function for creating a character
def character_creator(characters, races, classes, rg):
#       Display all possible races
    print("Available races:")
    for i, race in enumerate(races, 1):
        print(f"{i}. {race['name']}")
#       Ask for race
    character_race = choice_input(["1", "2", "3", "4", "5"], "What race would you like? (Enter number): ").strip()
#       Display all possible classes
    print("Available classes:")
    for i, cls in enumerate(classes, 1):
        print(f"{i}. {cls['name']}")
#       Ask for class
    character_class = choice_input(["1", "2", "3", "4", "5", "6", "7"], "What class would you like? (Enter number): ").strip()
#   Infinite loop
    while True:
#       Ask for name
       character_name = input("What name do you want for your character? ").strip().title()
#       If that name exists
       if character_name in characters:
#           Tell them that they must try again with a name not already used
           print("That name already exists. Please try again.")
#       Otherwise if that name doesn’t even exist
       elif character_name not in characters:
#           End the infinite loop
           break
#   Run the attribute dice roller from last year
    strength, intelligence, wisdom,  charisma, constitution, dexterity = attribute_roller()
#       Display the possible skill for the user
    print("Your possible skills are: ")
    skills = ["Archery", "Swordsmanship", "Magic", "Stealth", "Healing", "Intimidation"]
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill}")
#       Let them choose their skill
    character_skill = choice_input(["1", "2", "3", "4", "5", "6"], "What skill would you like? (Enter number): ").strip()
    character_race = races[int(character_race) - 1]["name"]
    character_class = classes[int(character_class) - 1]["name"]
    character_skill = skills[int(character_skill) - 1]
    return Character(character_name, character_race, character_class, character_skill, strength, intelligence, wisdom, charisma, dexterity, constitution, [], 0, backstory=rg.random_backstory(character_name, character_class, character_race), description=rg.random_description(character_name))

def backstory_creator(character, character_class, character_race):
    random_number = random.choice([1, 2, 3, 4])
    if random_number == 1:
        return f"{character} used to be a {fake.job()}. Then one day, he left his parents {fake.name_male()} and {fake.name_female()} on a work trip, only to find them dead when returning. Now, {character} is on a quest to find and get revenge on the killer of his parents. "
    elif random_number == 2:
        return f"{character}, the {character_class}, discovers a hidden map in {fake.name_male()}'s (His father) belongings that leads to a cursed treasure. {fake.name_female()} (His mother) warns them, but fate cannot be stopped. "
    elif random_number == 3:
        return f"As a young {character_race}, {character} watched as a rival clan destroyed their village and family. Sworn to justice, {character} now hunts the clan across the land. "
    elif random_number == 4:
        return f"{character}, the {character_class}, inherits a mysterious family heirloom after his father and mother - {fake.name_male()} and {fake.name_female()}'s - untimely death. It holds the key to defeating a powerful enemy threatening the kingdom. "
    elif random_number == 5:
        return f"{character}, a {character_class} of {character_race} descent, accidentally awakens an ancient curse while exploring {fake.city()}. Now they must find a way to undo the curse before it destroys everything they love. "
    elif random_number == 6:
        return f"{character} once served in the royal guard, but after a betrayal by a close friend, they were framed for the murder of {fake.name()}. Now, {character} seeks to clear their name and find the true culprit. "
    elif random_number == 7:
        return f"Orphaned as a {character_race} child, {character} was raised by wandering mercenaries. Learning the ways of a {character_class}, they now seek to uncover their mysterious heritage and confront the enemies who destroyed their family. "

def description(character, character_race):
    hair_colors = ["blonde", "brown", "black", "red", "white", "gray"]
    eye_colors = ["blue", "green", "brown", "hazel", "gray", "amber"]
    builds = ["slim", "athletic", "muscular", "stocky", "lean", "curvy"]
    heights = ["short", "average height", "tall", "towering"]
    distinguishing_features = [
        "a scar across the cheek",
        "a tattoo on the arm",
        "piercing eyes",
        "freckles across the nose",
        "a charismatic smile",
        "long flowing hair", 
        "a huge beard"
    ]
    if character_race == "orc":
        heights = ["tall", "towering"]
    elif character_race == "dwarf" or character_race == "halfling":
        heights = ["very short", "short"]
    description = (
        f"{character} has {random.choice(hair_colors)} hair, "
        f"{random.choice(eye_colors)} eyes, and a {random.choice(builds)} build. "
        f"They are {random.choice(heights)}, with {random.choice(distinguishing_features)}."
    )
    return description

def generate_quest():
    actions = ["rescue", "retrieve", "assassinate", "escort", "explore", "protect", "investigate"]
    return f"Your quest is to {random.choice(actions)} {random.choice([fake.name(), f'the {fake.word()} artifact', f'a {fake.word()} beast'])} in {random.choice([fake.city(), f'the {fake.word()} forest', f'{fake.word()} ruins'])}. "

#search character function
def view_character(character_list):
    if not character_list:
        print("No characters created yet.")
        return
    print("\nCharacters:")
    character_list = list(character_list.values())
    for i, c in enumerate(character_list, 1):
        print(f"{i}. {c.name} ({c.race} {c.char_class})")
    choice = input("Select a character by number: ").strip()
    try:
        char = character_list[int(choice)-1]
        print(f"\nName: {char.name}\nRace: {char.race}\nClass: {char.char_class}")
        print(f"Skill: {char.skill}\nBackstory: {char.backstory}\nDescription: {char.description}")
        # Visualization choice
        viz_choice = input("View attributes as: \n1. View attributes in a bar chart \n2. View attributes in a radar chart \n3. Manage inventory \n> ").strip()
        if viz_choice == "1":
            DataVisualization.plot_bar(char)
        elif viz_choice == "2":
            DataVisualization.plot_radar(char)
        elif viz_choice == "3":
            manage_inventory(char.inventory, char.inv_weight, char.strength * 5)
        else:
            print("Skipping visualization.")
    except (IndexError, ValueError):
        print("Invalid selection.")

def compare_characters(character_list):
    character_list = list(character_list.values())
    if len(character_list) < 2:
        print("Need at least 2 characters to compare.")
        return
    print("Characters available:")
    for i, c in enumerate(character_list, 1):
        print(f"{i}. {c.name}")
    selections = input("Select two characters by numbers, separated by comma (e.g., 1,2): ").split(",")
    try:
        c1 = character_list[int(selections[0].strip())-1]
        c2 = character_list[int(selections[1].strip())-1]
        # Create dataframe for comparison
        df = pd.DataFrame([c1.to_dict(), c2.to_dict()])
        print("\nAttribute comparison:")
        print(df[["Name","Strength","Intelligence","Wisdom","Charisma","Dexterity","Constitution"]])
        # Plot side by side
        DataVisualization.plot_bar(c1)
        DataVisualization.plot_bar(c2)
    except Exception as e:
        print("Invalid selection.", e)

def analyze_characters(character_list):
    if not character_list:
        print("No characters to analyze.")
        return
    analyzer = StatisticalAnalyzer(list(character_list.values()))
    print(analyzer.summary_statistics())
    for i in ["strength", "intelligence", "dexterity", "constitution", "wisdom", "charisma"]:
        top = analyzer.sort_characters(i).iloc[0]
        print(f"\nCharacter with highest {i}: {top['Name']} ({top[i]})")

def multi_radar(characters):
    attributes = ["Strength", "Intelligence", "Wisdom", "Charisma", "Dexterity", "Constitution"]
    num_attrs = len(attributes)
    angles = np.linspace(0, 2 * np.pi, num_attrs, endpoint=False).tolist()
    angles += angles[:1]  # close the circle
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)
    for char in characters:
        values = [
            char.strength, char.intelligence, char.wisdom, 
            char.charisma, char.dexterity, char.constitution
        ]
        values += values[:1]  # close the circle
        ax.plot(angles, values, label=char.name)
        ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes)
    ax.set_yticks(range(0, 21, 5))
    ax.set_title("Multi-Character Radar Chart")
    plt.legend(loc='upper right')
    plt.show()

#manage inventory function
def manage_inventory(items_in_inv, inv_weight, weight_limit):
   while True:
       user_choice = input("Would you like to: \n1. Add an item \n2. Equip a pre-existent item \n3. Delete an item \n4. View inventory \n5. Leave inventory\nInsert number: ").strip()
       if user_choice == '1':
           if inv_weight >= weight_limit:
               print("You can't add anything - inventory is full!")
           else:
               item_name = input("Enter item name: ").strip().title()
               try:
                   item_weight = int(input("Enter item weight: ").strip())
                   if inv_weight + item_weight <= weight_limit:
                       items_in_inv.append({"name": item_name, "weight":
                       item_weight})
                       inv_weight += item_weight
                       print(f"Added {item_name}!")
                   else:
                       print("Item too heavy for remaining capacity.")
               except ValueError:
                   print("Invalid weight input.")
       elif user_choice == '2':
           if not items_in_inv:
               print("Nothing in inventory to equip!")
           else:
               for i, item in enumerate(items_in_inv, 1):
                   print(f"{i}. {item['name']} (Weight: {item['weight']})")
               try:
                   choice = int(input("Select item number: ").strip()) - 1
                   if 0 <= choice < len(items_in_inv):
                       print(f"Equipped {items_in_inv[choice]['name']}!")
                   else:
                       print("Invalid selection.")
               except ValueError:
                   print("Invalid input.")
       elif user_choice == '3':
           if not items_in_inv:
               print("Nothing in inventory to delete!")
           else:
               for i, item in enumerate(items_in_inv, 1):
                   print(f"{i}. {item['name']}")
               try:
                   choice = int(input("Select item to delete: ").strip()) - 1
                   if 0 <= choice < len(items_in_inv):
                       removed = items_in_inv.pop(choice)
                       inv_weight -= removed['weight']
                       print(f"Deleted {removed['name']}!")
                   else:
                       print("Invalid selection.")
               except ValueError:
                   print("Invalid input.")
       elif user_choice == '4':
           if not items_in_inv:
               print("Inventory is empty!")
           else:
               print("\nYour Inventory")
               for i, item in enumerate(items_in_inv, 1):
                   print(f"{i}. {item['name']} (Weight: {item['weight']})")
               print(f"Total weight: {inv_weight}/{weight_limit}\n")
       elif user_choice == '5':
           break
       else:
           print("Invalid input. Please try again.")

#Display items function
def display_items(items_in_inv):
   if not items_in_inv:
       print("No items to display.")
   else:
       print("\nYour Items:")
       for i, item in enumerate(items_in_inv, 1):
           print(f"{i}. {item['name']} (Weight: {item['weight']})")
       print()


def attribute_roller():
   def checker(key):
       while True:
           attribute = input(f"Which roll do you want to choose for your {key}? ")
           if attribute in attribute_rolls:
               attribute_rolls.remove(attribute)
               for i in attribute_rolls:
                   print(i)
               return attribute
   attribute_rolls = []
   print("Your attribute options are: ")
   for i in range(6):
       attribute_rolls.append(str(random.randint(1,6) + random.randint(1,6) + random.randint(1,6)))
       print(attribute_rolls[i])
   strength = int(checker("strength"))
   intelligence = int(checker("intelligence"))
   wisdom = int(checker("wisdom"))
   dexterity = int(checker("dexterity"))
   charisma = int(checker("charisma"))
   constitution = int(checker("constitution"))
   return strength, intelligence, wisdom,  charisma, constitution, dexterity

def plot_attributes(character_data, character_name):
    attributes = ["strength", "intelligence", "wisdom", "charisma", "dexterity", "constitution"]
    values = [int(character_data[attr]) for attr in attributes]
    plt.figure(figsize=(8,5))
    plt.bar(attributes, values, color='skyblue')
    for i, v in enumerate(values):
        plt.text(i, v + 0.2, str(v), ha='center', fontsize=10)
    plt.title(f"{character_name}'s Attributes")
    plt.ylabel('Value')
    plt.ylim(0, max(values) + 5)
    plt.show()

def save(characters):
    saving = []
    for char in characters.values():
        saving.append(char.to_dict())
    save_csv("individual_projects/character_creator/docs/characters.csv", saving)

def character_dashboard(character_list):
    df = pd.DataFrame([char.to_dict() for char in character_list])
    attrs = ["Strength","Intelligence","Wisdom","Charisma","Dexterity","Constitution"]
    df[attrs].plot(kind='bar', figsize=(10,6))
    plt.title("Character Portfolio Overview")
    plt.ylabel("Attribute Value")
    plt.show()
    print("\nAverage Attributes Across Characters:")
    print(df[attrs].mean())

#main menu function
def main(characters, races, classes):
    rg = RandomGenerator()
#   Infinite loop
    while True:
        #Ask the user if they want to 1. Quit 2. Create a character 3. Find a character
        check = choice_input(["1", "2", "3", "4", "5", "6"], "Do you want to: \n1. Create a character \n2. Find a character \n3. Compare characters \n4. Get a quest \n5. Analyze characters \n6. Quit \n").strip()
#       If they chose 1
        if check == '1':
            new_character = character_creator(characters, races, classes, rg)
            characters[new_character.name] = new_character
            #Call the function to create a character
        #Otherwise if they chose 2
        elif check == '2':
            #Call the function to find a character
            view_character(characters)
        #Otherwise if they chose 3
        elif check == "3":
            choice = choice_input(["1", "2"], "Do you want to look them through: \n1. Bar charts \n2. Radar charts \n> ")
            if choice == "1":
                compare_characters(characters)
            elif choice == "2":
                multi_radar(characters)
        #Otherwise if they chose 4
        elif check == "4":
            print(generate_quest())
        elif check == "5":
            choice = choice_input(["1", "2"], "Do you want to: \n1. See the characters with the best stats \n2. See the average attributes of all the characters \n> ")
            if choice == "1":
                analyze_characters(characters)
            elif choice == "2":
                character_dashboard(characters)
        elif check == '6':
            #Break the infinite loop
            break
        save(characters)

#call main menu function
main(characters, races, classes)
