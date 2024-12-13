import matplotlib.pyplot as plt
import random
from datetime import timedelta

"""
    Driver module to be used to run our program.
    This python module runs the simulation and collections information on it.
    It will run the simulation for a select amount of ticks and every tick the 
    information on the program will outputed. The idea of this simulation is 
    to simulate the introduction of an invasive species and its impact on an exsisting
    ecosystem. 
    
    Invasive flower gives more pollen than the other flowers in the ecosystem
    The bees gravitate towards that flower

    Author: Gavin Barro and Austin Earl
    Version: 10/15/2024
"""

class Flower:
    MAX_AGE: int = 20
    
    def __init__(self, age: int, species: str, flower_seeds: int, lifespan: int, 
                 nectar_regeneration:float, start_of_bloom: int, flower_nectar: float, occupied: bool):
        self._age = age
        self._species = species
        self._flower_seeds = flower_seeds
        self._lifespan = lifespan
        self._nectar_regeneration = nectar_regeneration
        self._start_of_bloom = start_of_bloom
        self._flower_nectar = flower_nectar
        self._occupied = occupied
        self._number_visits = 0
        
       # Age
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value

    # Species
    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, value: str) -> None:
        self._species = value

    # Flower Seeds
    @property
    def flower_seeds(self) -> int:
        return self._flower_seeds

    @flower_seeds.setter
    def flower_seeds(self, value: int) -> None:
        self._flower_seeds = value

    # Lifespan
    @property
    def lifespan(self) -> int:
        return self._lifespan

    @lifespan.setter
    def lifespan(self, value: int) -> None:
        self._lifespan = value

    # Nectar Regeneration
    @property
    def nectar_regeneration(self) -> float:
        return self._nectar_regeneration

    @nectar_regeneration.setter
    def nectar_regeneration(self, value: float) -> None:
        self._nectar_regeneration = value

    # Start of Bloom
    @property
    def start_of_bloom(self) -> int:
        return self._start_of_bloom

    @start_of_bloom.setter
    def start_of_bloom(self, value: int) -> None:
        self._start_of_bloom = value

    # Flower Nectar
    @property
    def flower_nectar(self) -> float:
        return self._flower_nectar

    @flower_nectar.setter
    def flower_nectar(self, value: float) -> None:
        self._flower_nectar = value

    # Occupied
    @property
    def occupied(self) -> bool:
        return self._occupied

    @occupied.setter
    def occupied(self, value: bool) -> None:
        self._occupied = value

    # number_visits
    @property
    def number_visits(self) -> int:
        return self.number_visits
    
    @occupied.setter
    def number_visits(self, value: int) -> None:
        self._number_visits += value

    def increase_visits(self):
        self._number_visits += 1

    def update_flower(self, value: int) -> int:
        self.occupied = True
        curr_flower_nectar = self._flower_nectar - value + self._nectar_regeneration
        if curr_flower_nectar > 0:
            self._flower_nectar = curr_flower_nectar
        else:
            value = self._flower_nectar
            self._flower_nectar = 0
        return value
    
    def produce_seeds(self) -> bool:
        if self._number_visits >= 3:
            return True
        return False

    def produce_seeds_weighted(self) -> bool:
        if self._number_visits >= 4 and self._species != "Invasive Flower":
            return True
        elif self._number_visits >= 2 and self._species == "Invasive Flower":
            return True
        return False

    def age_flower(self) -> bool:
        """Aging the flower over time."""
        self.age += 1
        if self.age > self.MAX_AGE:
            return True  # Flower dies after reaching lifespan
        return False
    
    def regenerate_nectar(self) -> None:
        """ Regenerate nectar based on the flower's nectar regeneration rate. """
        self.flower_nectar += self.nectar_regeneration
        if self.flower_nectar > 100:  # Maximum nectar limit
            self.flower_nectar = 100

        

class Hive:
    '''
    producing-bees
    season-start
    season-end
    storage-nectar
    has-seed?
    '''

    # Make a new bee every 10 ticks
    # When bees reach maximum nectar, they visit the hive - reset bees nectar to 0

    def __init__(self, age: int, species: str, producing_bees: bool, season_start: int, 
    season_end: int, storage_nectar: int, has_seed: bool):
        self._age = age
        self._species = species
        self._producing_bees = producing_bees
        self._season_start = season_start
        self._season_end = season_end
        self._storage_nectar = storage_nectar
        self._has_seed = has_seed

    # Age
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value

    # Species
    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, value: str) -> None:
        self._species = value

    # Producing Bees
    @property
    def producing_bees(self) -> bool:
        return self._producing_bees

    @producing_bees.setter
    def producing_bees(self, value: bool) -> None:
        self._producing_bees = value

    # Season Start
    @property
    def season_start(self) -> timedelta:
        return self._season_start

    @season_start.setter
    def season_start(self, value: timedelta) -> None:
        self._season_start = value

    # Season End
    @property
    def season_end(self) -> timedelta:
        return self._season_end

    @season_end.setter
    def season_end(self, value: timedelta) -> None:
        self._season_end = value

    # Storage Nectar
    @property
    def storage_nectar(self) -> int:
        return self._storage_nectar

    @storage_nectar.setter
    def storage_nectar(self, value: int) -> None:
        self._storage_nectar = value

    # Has Seed
    @property
    def has_seed(self) -> bool:
        return self._has_seed

    @has_seed.setter
    def has_seed(self, value: bool) -> None:
        self._has_seed = value
    
    def store_nectar(self, nectar: int) -> None:
        self._storage_nectar += nectar


class Bee:
    MAX_NECTAR = 19

    def __init__(self, age: int, species: str, previous_flower, 
                 destination , home_hive: Hive, collection_start_time: int, current_flower,  
                 count_carry_nectar: int, pollen: int):
        self._age = age
        self._species = species
        self._previous_flower = previous_flower
        self._destination = destination
        self._home_hive = home_hive
        self._collection_start_time = collection_start_time
        self._current_flower = current_flower
        self._count_carry_nectar = count_carry_nectar
        self._pollen = pollen
        
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter 
    def age(self, value: int) -> None:
        self._age = value  
        
    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value: str) -> None:
        self._species = value

    @property
    def previous_flower(self):
        return self._previous_flower

    @previous_flower.setter
    def previous_flower(self, value: Flower) -> None:
        self._previous_flower = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value: Flower) -> None:
        self._destination = value

    @property
    def home_hive(self) -> Hive:
        return self._home_hive

    @home_hive.setter
    def home_hive(self, value: Hive) -> None:
        self._home_hive = value

    @property
    def collection_start_time(self) -> int:
        return self._collection_start_time

    @collection_start_time.setter
    def collection_start_time(self, value: int) -> None:
        self._collection_start_time = value

    @property
    def current_flower(self):
        return self._current_flower

    @current_flower.setter
    def current_flower(self, value: Flower) -> None:
        self._current_flower = value

    @property
    def count_carry_nectar(self) -> int:
        return self._count_carry_nectar

    @count_carry_nectar.setter
    def count_carry_nectar(self, value: int) -> None:
        self._count_carry_nectar = value

    @property
    def pollen(self) -> int:
        return self._pollen

    @pollen.setter
    def pollen(self, value: int) -> None:
        self._pollen = value  

    def visit_flower(self, iteration: int) -> None:
        value = 0
        if self._current_flower.species == "Invasive Flower":
            value = 6
        else:
            value = 3
        self._count_carry_nectar += self._current_flower.update_flower(value)
        self._current_flower.age_flower()

    def visit_hive(self) -> None:
        self.current_flower.occupied = False
        self._previous_flower = self.current_flower
        self._home_hive.store_nectar(self._count_carry_nectar)
        self._count_carry_nectar = 0

    def move_bee(self) -> None:
        self.current_flower.occupied = False
        self._previous_flower = self._current_flower
        self._current_flower = self._destination
        
    def increment_remove_age(self) -> bool:
        self.age += 1
        rand = random.randint(0, 100)
        if (self.age > 15 and rand > 70) or self.age >= 30:
            return True
        return False
    
class WeightedEcosystem:
    BEE_WAITTIME: int = 8
    NECTAR_DECREASE_RATE: int = 58
    
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

class Ecosystem:
    BEE_WAITTIME: int = 8
    NECTAR_DECREASE_RATE: int = 48
    
    def __init__(self, bees: list[Bee], flowers: list[Flower], hives: list[Hive]):
        self.bees = bees
        self.flowers = flowers
        self.hives = hives
        self.iterations = 0
        self.max_iterations = 1000
        self.flower_types = ["Invasive Flower", "Red Flower", "Blue Flower", "Green Flower"]
            

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
            if flower.produce_seeds():
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

def main() -> None:
    simulation1 = setup_simulation()
    simulation2 = setup_simulation()
    
    # Baseline simulation where invasive flowers don't dominate
    ecosystem1 = Ecosystem(simulation1["Bees"], simulation1["Flowers"], simulation1["Hives"])
    ecosystem1.simulation()
    #print(ecosystem1)
    
    # # Invasive flowers dominate because their nectar rewards are higher
    ecosystem2 = WeightedEcosystem(simulation2["Bees"], simulation2["Flowers"], simulation2["Hives"])
    ecosystem2.simulation()

def setup_simulation() -> dict[str, list]:
    """
    Sets up base components to our environment. This is our baseline simulation where invasive flowers don't dominate
    
    Returns:
        dict: our parameters for simulation 1
    """
    hives_list: list[Hive] = []
    for _ in range(2):
            age = 0
            species = "Hives"
            producing_bees = True
            season_start = 0
            season_end = 1000
            storage_nectar = 0
            has_seed = False
            curr_hive = Hive(age, species, producing_bees, season_start, season_end, storage_nectar, has_seed)
            hives_list.append(curr_hive)
    
    flowers_list: list[Flower] = []
    for _ in range(20):
            age = 0
            flower_seeds = 0
            species = "Red Flower"
            lifespan = 35
            nectar_regen = 1.5
            start = 0
            flower_nectar = 60
            occupied = False
            blocked_seeds = []
            curr_flower = Flower(age, species, flower_seeds, lifespan, nectar_regen, 
                                 start, flower_nectar, occupied)
            flowers_list.append(curr_flower)
            
    for _ in range(20):
        age = 0
        flower_seeds = 0
        species = "Blue Flower"
        lifespan = 35
        nectar_regen = 1.5
        start = 0
        flower_nectar = 60
        occupied = False
        blocked_seeds = []
        curr_flower = Flower(age, species, flower_seeds, lifespan, nectar_regen, 
                                 start, flower_nectar, occupied)
        flowers_list.append(curr_flower)
            
    for _ in range(20):
        age = 0
        flower_seeds = 0
        species = "Green Flower"
        lifespan = 30
        nectar_regen = 1.5
        start = 0
        flower_nectar = 60
        occupied = False
        blocked_seeds = []
        curr_flower = Flower(age, species, flower_seeds, lifespan, nectar_regen, 
                                 start, flower_nectar, occupied)
        flowers_list.append(curr_flower)
    
    for _ in range(10):
        age = 0
        flower_seeds = 0
        species = "Invasive Flower"
        lifespan = 45
        nectar_regen = 3
        start = 0
        flower_nectar = 60
        occupied = False
        blocked_seeds = []
        curr_flower = Flower(age, species, flower_seeds, lifespan, nectar_regen, 
                                 start, flower_nectar, occupied)
        flowers_list.append(curr_flower)
    
    bees_list: list[Bee] = []
    for _ in range(30):
        curr_age = 0
        curr_species = "Bee"
        previous_flower = None
        destination = None
        current_flower = None
        home_hive = hives_list[random.randint(0, len(hives_list) - 1)]
        collection_start_time = 0 # most recent time the bee has collected
        count_carry_nectar = 0
        pollen = 0
        bee = Bee(curr_age, curr_species, previous_flower, destination, home_hive, 
                      collection_start_time, current_flower, count_carry_nectar, pollen)
        bees_list.append(bee)
    
    return {"Bees": bees_list, "Flowers": flowers_list, "Hives": hives_list}


if __name__ == "__main__":
    main()