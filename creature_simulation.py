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

# ===============================
# FlyingCreature Branch
# ===============================

class FlyingCreature(Creature):
class FireCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        if attack_power <= 100 and attack_power >= 0 :
            self.fire_level = attack_power
        else:
            return ValueError ("Attack power must be between 0 and 100")

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")
# SwimmingCreature Branch
# ===============================

class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.depth = 0

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def emit_fire(self):
        print(f"{self.name} Emmits Fire At {self.fire_level} Level.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} swoops down from altitude {self.altitude}!")
        print(f"{self.name} performs an aerial attack on {target.name} for {self.attack_power} damage!")
        print(f"{self.name} attacks from underwater at depth {self.depth}!")
        print(f"It splashes {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power
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

    print("=== FlyingCreature Tests ===\n")
    hawk = FlyingCreature("Sky Hawk", 50, 8)
    hawk.fly_to(120)
    print(f"Altitude should be 120 → Actual: {hawk.altitude}")

    dummy = Creature("Practice Dummy", 40, 0)
    hawk.attack(dummy)
    print(f"Dummy HP should be 32 → Actual: {dummy.hp}")
    dummy.attack(hawk)
    print()
    print("=== Tests Completed ===")
    print()
    print("=== SwimmingCreature Tests ===\n")
    serpent = SwimmingCreature("Aqua Serpent", 60, 7)
    serpent.dive_to(30)
    print(f"Depth should be 30 → Actual: {serpent.depth}")

    dummy = Creature("Practice Dummy", 40, 0)
    serpent.attack(dummy)
    print(f"Dummy HP should be 33 → Actual: {dummy.hp}")
    print()
    print("=== Tests Completed ===")
    print()
