import random
from bees import Bee
from hives import Hive
from flowers import Flower
import matplotlib.pyplot as plt 

class WeightedEcosystem:
    BEE_WAITTIME = 8
    NECTAR_DECREASE_RATE = 58
    
    def __init__(self, bees: list[Bee], flowers: list[Flower], hives: list[Hive]):
        self.bees = bees
        self.flowers = flowers
        self.hives = hives
        self.iterations = 0
        self.max_iterations = 1000
        self.flower_types = ["Invasive Flower", "Invasive Flower", "Invasive Flower", "Red Flower",
                             "Blue Flower", "Green Flower"]
            

    def simulation(self) -> None:
        """Run the simulation."""
        bee_counts = []
        hive1_nectar = []
        hive2_nectar = []
        red_flower_counts = []
        green_flower_counts = []
        blue_flower_counts = []
        invasive_flower_counts = []

        while self.iterations < self.max_iterations:
            self.tick(self.iterations)
            self.iterations += 1

            # Collect data for plotting
            bee_counts.append(len(self.bees))
            hive1_nectar.append(self.hives[0].storage_nectar)
            hive2_nectar.append(self.hives[1].storage_nectar)

            # Count flowers by type
            red_count = sum(1 for flower in self.flowers if flower.species == "Red Flower")
            green_count = sum(1 for flower in self.flowers if flower.species == "Green Flower")
            blue_count = sum(1 for flower in self.flowers if flower.species == "Blue Flower")
            invasive_count = sum(1 for flower in self.flowers if flower.species == "Invasive Flower")

            red_flower_counts.append(red_count)
            green_flower_counts.append(green_count)
            blue_flower_counts.append(blue_count)
            invasive_flower_counts.append(invasive_count)

        # Plot the data after the simulation
        self.plot_data(bee_counts, hive1_nectar, hive2_nectar, red_flower_counts, 
                    green_flower_counts, blue_flower_counts, invasive_flower_counts)

    def tick(self, iteration: int) -> None:
            self.update_bees_flowers(iteration)
            self.update_hives()
        
    def update_bees_flowers(self, iteration: int) -> None:
        if iteration == 0:
            for bee in self.bees:
                flower_type = random.choice(self.flower_types)
                flower_choice = None
                for flower in self.flowers:
                    if flower.species == flower_type and not flower.occupied:
                        flower_choice = flower
                        break

                if flower_choice == None:
                    flower_choice = random.choice(self.flowers)

                bee.current_flower = flower_choice
                bee.visit_flower(iteration)
        else:
            for bee in self.bees:
                if bee._count_carry_nectar >= bee.MAX_NECTAR:
                    bee.visit_hive()
                else:
                    flower_type = random.choice(self.flower_types)
                    flower_choice = None
                    for flower in self.flowers:
                        if flower.species == flower_type and not flower.occupied:
                            flower_choice = flower
                            break
                    if flower_choice == None:
                        flower_choice = random.choice(self.flowers)
                    bee.destination = flower_choice
                    if not flower_choice.occupied:
                        bee.move_bee()
                        bee.visit_flower(iteration)
                        bee.current_flower.increase_visits()
                if bee.increment_remove_age(): self.bees.remove(bee)
        
        for flower in self.flowers:
            flower.regenerate_nectar()
            if flower.produce_seeds_weighted():
                self.flowers.append(Flower(0, flower.species, 0, flower.lifespan, flower.nectar_regeneration,
                                           flower.start_of_bloom, 30, False))
            if flower.age_flower():
                self.flowers.remove(flower)
                
    def update_hives(self) -> None:
        for hive in self.hives:
            if hive.producing_bees and hive.storage_nectar > 5:
                rand_flower: Flower = random.choice(self.flowers)
                new_bee = Bee(0, "Bee", None, None, hive, 0, rand_flower, 0, 0)
                new_bee.home_hive.storage_nectar -= self.NECTAR_DECREASE_RATE
                self.bees.append(new_bee)
              
    def plot_data(self, bee_counts: list[int], hive1_nectar: list[int], hive2_nectar: list[int], 
              red_counts: list[int], green_counts: list[int], blue_counts: list[int], 
              invasive_counts: list[int]) -> None:
        plt.figure(figsize=(10, 10))

        # Plot the number of bees over time
        plt.subplot(4, 1, 1)
        plt.plot(bee_counts, label="Number of Bees", color="yellow")
        plt.title("Ecosystem Simulation: Number of Bees")
        plt.xlabel("Iterations")
        plt.ylabel("Bee Count")
        plt.legend()

        # Plot the nectar stored in each hive over time
        plt.subplot(4, 1, 2)
        plt.plot(hive1_nectar, label="Hive 1 Nectar", color="orange")
        plt.plot(hive2_nectar, label="Hive 2 Nectar", color="brown")
        plt.title("Ecosystem Simulation: Nectar Levels in Hives")
        plt.xlabel("Iterations")
        plt.ylabel("Nectar Stored")
        plt.legend()

        # Plot the counts for each flower type
        plt.subplot(4, 1, 3)
        plt.plot(red_counts, label="Red Flowers", color="red")
        plt.plot(green_counts, label="Green Flowers", color="green")
        plt.plot(blue_counts, label="Blue Flowers", color="blue")
        plt.plot(invasive_counts, label="Invasive Flowers", color="black")
        plt.title("Ecosystem Simulation: Flower Counts by Species")
        plt.xlabel("Iterations")
        plt.ylabel("Flower Count")
        plt.legend()

        # Display the plots
        plt.tight_layout()
        plt.show()
