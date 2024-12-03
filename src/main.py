import matplotlib.pyplot as plt
from ecosystem import Ecosystem
import random
from bees import Bee
from hives import Hive
from flowers import Flower
from seeds import Seed

"""
    Driver module to be used to run our program.
    TODO: This python module runs the simulation and collections information on it.
    It will run the simulation for a select amount of ticks and every tick the 
    information on the program will outputed. The idea of this simulation is 
    to simulate the introduction of an invasive species and its impact on an exsisting
    ecosystem. 
    
    Invasive flower gives more pollen than the other flowers in the ecosystem
    The bees gravitate towards that flower

    Author: Gavin Barro and Austin Earl
    Version: 10/15/2024
"""


def main() -> None:
    simulation1 = setup_simulation1()
    # simulation2 = setup_simulation2()
    # simulation3 = setup_simulation3()
    
    # Baseline simulation where invasive flowers don't dominate
    ecosystem1 = Ecosystem(simulation1["Bees"], simulation1["Flowers"], simulation1["Hives"], 1)
    ecosystem1.simulation()
    print(ecosystem1)
    
    # # Invasive flowers dominate because their nectar rewards are higher
    # ecosystem2 = Ecosystem(simulation2["Bees"], simulation2["Flowers"], simulation2["Hives"], simulation2["Seeds"])ß



def setup_simulation1() -> dict[str, list]:
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
    
    seed_list: list[Seed] = []
    for _ in range(60):
        age = 0
        cur_flower = flowers_list[random.randint(0, len(flowers_list) - 1)]
        species = cur_flower.species
        life_span = cur_flower.lifespan
        start_of_bloom = cur_flower.start_of_bloom
        occupied = cur_flower.occupied
        nectar_regn = cur_flower.nectar_regeneration
        active = False
        cur_seed = Seed(age, species, life_span, start_of_bloom, occupied, nectar_regn, active)
        seed_list.append(cur_seed)
    
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
    
    return {"Bees": bees_list, "Flowers": flowers_list, "Hives": hives_list, "Seeds": seed_list}


def setup_simulation2() -> dict[str, list]:
    """
    Sets up base components to our environment

    Returns:
        dict: our parameters for simulation 2
    """
    
    pass


if __name__ == "__main__":
    main()