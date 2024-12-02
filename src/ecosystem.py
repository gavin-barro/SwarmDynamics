import random
from bees import Bee
from hives import Hive
from seeds import Seed
from flowers import Flower
import matplotlib.pyplot as plt 

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
                # while flower_choice.flower_nectar > 0 and not flower_choice.occupied:
                bee.current_flower = flower_choice
                bee.visit_flower(iteration)
        else:
            for bee in self.bees:
                if bee._count_carry_nectar >= bee.MAX_NECTAR:
                    bee.visit_hive()
                else:
                    flower_choice: Flower = random.choice(self.flowers)  # Bee chooses a flower randomly
                    bee.destination = flower_choice
                    if not flower_choice.occupied:
                        bee.move_bee()
                        bee.visit_flower(iteration)
                if bee.increment_remove_age(): self.bees.remove(bee)
        
        for flower in self.flowers:
            if not flower.age_flower():
                self.flowers.remove(flower)
                

    
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
    
    def plot_data(self, bee_counts, nectar_storages, flower_counts) -> None:
        plt.figure(figsize=(10, 6))

        # Plot the number of bees over time
        plt.subplot(3, 1, 1)
        plt.plot(bee_counts, label="Number of Bees", color="blue")
        plt.title("Ecosystem Simulation: Number of Bees")
        plt.xlabel("Iterations")
        plt.ylabel("Bee Count")
        plt.legend()

        # Plot the total nectar stored in all hives over time
        plt.subplot(3, 1, 2)
        plt.plot(nectar_storages, label="Total Nectar in Hives", color="green")
        plt.title("Ecosystem Simulation: Total Nectar in Hives")
        plt.xlabel("Iterations")
        plt.ylabel("Nectar Stored")
        plt.legend()

        # Plot the number of flowers over time (or by species if needed)
        plt.subplot(3, 1, 3)
        plt.plot(flower_counts, label="Number of Flowers", color="red")
        plt.title("Ecosystem Simulation: Number of Flowers")
        plt.xlabel("Iterations")
        plt.ylabel("Flower Count")
        plt.legend()

        # Display the plots
        plt.tight_layout()
        plt.show()