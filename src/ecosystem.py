import random
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
        # while self.iterations < self.max_iterations:
        #     self.update_ecosystem()
        #     self.iterations += 1
        for i in range(20):
            self.tick(i)

    def tick(self, iteration: int) -> None:
        """Update the states of bees, flowers, hives, and seeds."""
        self.update_bees(iteration)
        self.update_flowers()
        self.update_hives()
        self.update_seeds()
        #  TODO
        
    def update_bees(self) -> None:
        for bee in self.bees:
            flower_choice: Flower  = random.choice(self.flowers)  # Bee chooses a flower randomly
            if bee.visit_flower(flower_choice):
                # Flower successfully pollinated
                flower_choice.produce_seeds()  # Produce seeds if pollinated
    
    def update_flowers(self) -> None:
        pass
    
    def update_hives(self) -> None:
        pass
    
    def update_seeds(self) -> None:
        pass