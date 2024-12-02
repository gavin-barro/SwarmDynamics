import random as rand
from bees import Bee
from hives import Hive
from seeds import Seed
from flowers import Flower

class Ecosystem:
    BEE_WAITTIME: int = 8
    
    def __init__(self, bees: list[Bee], flowers: list[Flower], hives: list[Hive], seeds: list[Seed]):
        self.bees = bees
        self.flowers = flowers
        self.hives = hives
        self.seeds = seeds
        self.iterations = 0
        self.max_iterations = 1000
            

    def simulation(self) -> None:
        """Run the simulation."""
        while self.iterations < self.max_iterations:
            self.update_ecosystem()
            self.iterations += 1

    def update_ecosystem(self):
        """Update the states of bees, flowers, hives, and seeds."""
        self.update_bees()
        self.update_flowers()
        self.update_hives()
        self.update_seeds()
        #  TODO