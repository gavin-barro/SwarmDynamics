import random
from bees import Bee
from hives import Hive
from seeds import Seed
from flowers import Flower

class Ecosystem:
    BEE_WAITTIME: int = 8
    
    def __init__(self, bees: list[Bee], flowers: list[Flower], hives: list[Hive], seeds: list[Seed], simulation_num: int):
        self.bees = bees
        self.flowers = flowers
        self.hives = hives
        self.seeds = seeds
        self.simulation_num = simulation_num
        self.iterations = 0
        self.max_iterations = 1000
            

    def simulation(self) -> None:
        """Run the simulation."""
        # while self.iterations < self.max_iterations:
        #     self.update_ecosystem()
        #     self.iterations += 1
        for i in range(20):
            self.tick(i, self.simulation_num)

    def tick(self, iteration: int, simulation_num: int) -> None:
        """Update the states of bees, flowers, hives, and seeds."""
        if simulation_num == 1:
            self.update_bees_1(iteration)
            self.update_flowers_1()
            self.update_hives_1()
            self.update_seeds_1()
        #  TODO
        else:
            self.update_bees_2(iteration)
            self.update_flowers_2()
            self.update_hives_2()
            self.update_seeds_2()
        
    def update_bees_1(self, iteration: int) -> None:
        for bee in self.bees:
            flower_choice: Flower  = random.choice(self.flowers)  # Bee chooses a flower randomly
            if bee.visit_flower(flower_choice, iteration):
                # Flower successfully pollinated
                flower_choice.produce_seeds()  # Produce seeds if pollinated
    
    def update_flowers_1(self) -> None:
        pass
    
    def update_hives_1(self) -> None:
        pass
    
    def update_seeds_1(self) -> None:
        pass
    
    # Simulation 2
    def update_bees_2(self, iteration: int) -> None:
        for bee in self.bees:
            #TODO make it so it leans towards invasive species
            flower_choice: Flower  = random.choice(self.flowers)
            if bee.visit_flower(flower_choice, iteration):
                # Flower successfully pollinated
                flower_choice.update_flower()  # Produce seeds if pollinated
    
    def update_flowers_2(self) -> None:
        pass
    
    def update_hives_2(self) -> None:
        pass
    
    def update_seeds_2(self) -> None:
        pass