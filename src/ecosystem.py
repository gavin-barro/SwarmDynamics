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
            self.update_bees_flowers_1(iteration)
            self.update_hives_1()
            self.update_seeds_1()
        #  TODO
        else:
            self.update_bees_flowers_2(iteration)
            self.update_hives_2()
            self.update_seeds_2()
        
    def update_bees_flowers_1(self, iteration: int) -> None:
        if iteration == 0:
            for bee in self.bees:
                flower_choice: Flower  = random.choice(self.flowers)  # Bee chooses a flower randomly
                while flower_choice.flower_nectar > 0 and not flower_choice.occupied:
                    flower_choice: Flower  = random.choice(self.flowers)
                bee._current_flower(flower_choice)
                bee.visit_flower(iteration)
        else:
            for bee in self.bees:
                if bee._count_carry_nectar >= bee.MAX_NECTAR:
                    bee.visit_hive()
                else:
                    flower_choice: Flower  = random.choice(self.flowers)  # Bee chooses a flower randomly
                    bee._destination(flower_choice)
                    if not flower_choice.occupied:
                        bee.move_bee()
                        bee.visit_flower(iteration)
                if bee.increment_remove_age(): self.bees.remove(bee)

    
    def update_hives_1(self) -> None:
        pass
    
    def update_seeds_1(self) -> None:
        pass
    
    # Simulation 2
    def update_bees_flowers_2(self, iteration: int) -> None:
        for bee in self.bees:
            #TODO make it so it leans towards invasive species
            flower_choice: Flower  = random.choice(self.flowers)
            if bee.visit_flower(flower_choice, iteration):
                # Flower successfully pollinated
                flower_choice.update_flower()  # Produce seeds if pollinated
    
    def update_hives_2(self) -> None:
        pass
    
    def update_seeds_2(self) -> None:
        pass