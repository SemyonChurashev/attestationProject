"""
Создать класс дерева. Дерево должно расти, обладать высотой, возрастом и при достижении
определенного возраста засыхать.
Вся история об изменении параметров дерева должна записываться в json файл.
Создать метод чтения из истории о состоянии дерева в определенный период времени
На основе класса "дерево" создать другие деревья ("ель", "дуб")
"""


import json
from datetime import datetime
from utils import definitions
import random


class Tree:
    def __init__(self, height=0, age=0, lifespan=100):
        self.height = height
        self.age = age
        self.lifespan = lifespan
        self.history = list()
        self.event_year = datetime.now().year
        self.event = "planted"
        self.alive = True
        self.save_history()

    def plant(self):
        while self.age <= self.lifespan and self.alive:
            self.age += 1
            self.height += 1
            self.event_year += 1
            self.event = "grow"
            if random.randrange(101) <= 2:
                self.event = "cut down a tree"
                self.alive = False
            elif random.randrange(101) >= 90:
                self.event = "nuclear war"
                self.lifespan -= 50
            elif random.randrange(101) == 50:
                self.event = "buried under a tree"
                self.lifespan += 10
            elif self.age > self.lifespan:
                self.event = "tree had totally dried up"
                self.alive = False
            self.save_history()

    def save_history(self):
        entry = {
            "year": self.event_year,
            "age": self.age,
            "height": self.height,
            "alive": self.alive,
            "event": self.event
        }
        self.history.append(entry)

        with open(definitions.TMP_DIR / 'tree_history.json', 'w+', ) as f:
            json.dump(self.history, f, indent=4, sort_keys=True)

    @classmethod
    def read_history(cls, filename="tree_history.json"):
        try:
            with open(definitions.TMP_DIR / filename, 'r') as f:
                history = json.load(f)
                print(json.dumps(history, indent=4))

        except (FileNotFoundError, ValueError):
            print("Файл не найден или пустой")
        return []


class PineTree(Tree):
    def __init__(self, height=0, age=0):
        super().__init__(height, age, lifespan=80)  # Ели обычно живут меньше


class OakTree(Tree):
    def __init__(self, height=0, age=0):
        super().__init__(height, age, lifespan=200)  # Дубы живут дольше


tree = OakTree()
tree.plant()
Tree.read_history()
