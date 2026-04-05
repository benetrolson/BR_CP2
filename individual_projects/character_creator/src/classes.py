import random
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fake = Faker()

class Character:
    def __init__(self, name, race, char_class, skill, strength, intelligence, wisdom,
                 charisma, dexterity, constitution, inventory=None, inv_weight=0, backstory=None, description=None):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.skill = skill
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.dexterity = dexterity
        self.constitution = constitution
        self.inventory = inventory or []
        self.inv_weight = inv_weight
        self.backstory = backstory or self.generate_backstory()
        self.description = description or self.generate_description()
    def generate_backstory(self):
        return f"{self.name}, a {self.char_class} of {self.race}, begins an epic adventure. "
    def generate_description(self):
        hair_colors = ["blonde", "brown", "black", "red", "white", "gray"]
        eye_colors = ["blue", "green", "brown", "hazel", "gray", "amber"]
        builds = ["slim", "athletic", "muscular", "stocky", "lean", "curvy"]
        heights = ["short", "average height", "tall", "towering"]
        return (f"{self.name} has {random.choice(hair_colors)} hair, "
                f"{random.choice(eye_colors)} eyes, a {random.choice(builds)} build, "
                f"and is {random.choice(heights)}.")
    def to_dict(self):
        return {
            "name": self.name,
            "race": self.race,
            "class": self.char_class,
            "skill": self.skill,
            "strength": self.strength,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "inventory": self.inventory,
            "inv_weight": self.inv_weight,
            "backstory": self.backstory,
            "description": self.description
        }

class RandomGenerator:
    def __init__(self):
        self.fake = Faker()
    def random_backstory(self, char_name, char_class, race):
        return f"{char_name}, a {char_class} of {race}, discovers a mysterious artifact in {self.fake.city()}."
    def random_description(self, char_name):
        hair_colors = ["blonde", "brown", "black", "red", "white", "gray"]
        eye_colors = ["blue", "green", "brown", "hazel", "gray", "amber"]
        return f"{char_name} has {random.choice(hair_colors)} hair and {random.choice(eye_colors)} eyes."
    def random_quest(self):
        quest_types = ["rescue", "retrieve", "assassinate", "escort", "explore"]
        targets = [self.fake.name(), f"the {self.fake.word()} artifact", f"a {self.fake.word()} beast"]
        locations = [self.fake.city(), f"the {self.fake.word()} forest", f"{self.fake.word()} castle"]
        return f"Your quest is to {random.choice(quest_types)} {random.choice(targets)} in {random.choice(locations)}."

class DataVisualization:
    @staticmethod
    def plot_bar(character):
        attrs = ["Strength", "Intelligence", "Wisdom", "Charisma", "Dexterity", "Constitution"]
        values = [character.strength, character.intelligence, character.wisdom, 
                  character.charisma, character.dexterity, character.constitution]
        plt.figure(figsize=(8,5))
        plt.bar(attrs, values, color='skyblue')
        for i, v in enumerate(values):
            plt.text(i, v + 0.2, str(v), ha='center')
        plt.title(f"{character.name}'s Attributes")
        plt.ylabel("Value")
        plt.show()
    @staticmethod
    def plot_radar(character):
        attrs = ["Strength", "Intelligence", "Wisdom", "Charisma", "Dexterity", "Constitution"]
        values = [character.strength, character.intelligence, character.wisdom, 
                  character.charisma, character.dexterity, character.constitution]
        values += values[:1]
        angles = np.linspace(0, 2 * np.pi, len(attrs), endpoint=False).tolist()
        angles += angles[:1]
        fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
        ax.plot(angles, values, 'o-', linewidth=2)
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(np.degrees(angles[:-1]), attrs)
        plt.title(f"{character.name}'s Attributes (Radar Chart)")
        plt.show()

class StatisticalAnalyzer:
    def __init__(self, character_list):
        self.df = pd.DataFrame([char.to_dict() for char in character_list])
    def summary_statistics(self):
        return self.df.describe()
    def compare_characters(self, char_names):
        return self.df[self.df["name"].isin(char_names)]
    def filter_by_attribute(self, attribute, threshold):
        return self.df[self.df[attribute] >= threshold]
    def sort_characters(self, attribute, ascending=False):
        return self.df.sort_values(by=attribute, ascending=ascending)

