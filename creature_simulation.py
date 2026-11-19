class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"

class FireCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        if attack_power <= 100 and attack_power >= 0 :
            self.fire_level = attack_power
        else:
            return ValueError ("Attack power must be between 0 and 100")


    def emit_fire(self):
        print(f"{self.name} Emmits Fire At {self.fire_level} Level.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} Emmmits Fire at {self.fire_level}% !")
        print(f"It Burns {target.name} for {self.fire_level} damage!")
        target.hp -= self.fire_level
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")



if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)  # Expected: Goblin (HP: 30)
    print()

    # Test 2: Basic attack
    dragon = FireCreature("Dragon", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Dragon attacks Sheep")
    dragon.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.hp}")
    print()

    

    print("=== Tests Completed ===")
    print()