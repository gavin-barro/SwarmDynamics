import random as rand
from bees import Bee

# this is for simulation 1
class Ecosystem:
    BEE_WAITTIME: int = 8
    
    def __init__(self):
        self.bees = []
        self.flowers = []
        self.hives = []
        self.seeds = []
        self.iterations = 0
        self.max_iterations = 1000
    
    def make_bees(self) -> None:
        for i in range(30):
            curr_age = 0
            curr_species = "Bee"
            choosen_flower = None
            previous_flower = None
            home_hive = self.hives[rand(0, len(self.hives) - 1)]
            collection_start_time = 0 # most recent time the bee has collected
            count_carry_nectar = 0
            pollen = 0
            bee = Bee(curr_age, curr_species, choosen_flower, previous_flower, home_hive, 
                      collection_start_time, count_carry_nectar, pollen)
            self.bees.append(bee)

    def make_flowers() -> None:
        pass

    def make_hives() -> None:
        pass

    def make_seeds() -> None:
        pass

    def simulation() -> None:
        pass