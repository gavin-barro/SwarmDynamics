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
    
    # def make_bees(self) -> None:
    #     for i in range(30):
    #         curr_age = 0
    #         curr_species = "Bee"
    #         choosen_flower = None
    #         previous_flower = None
    #         home_hive = self.hives[rand(0, len(self.hives) - 1)]
    #         collection_start_time = 0 # most recent time the bee has collected
    #         count_carry_nectar = 0
    #         pollen = 0
    #         bee = Bee(curr_age, curr_species, choosen_flower, previous_flower, home_hive, 
    #                   collection_start_time, count_carry_nectar, pollen)
    #         self.bees.append(bee)

    # def make_flowers(self) -> None:
    #     for i in range(20):
    #         age = 0
    #         flower_seeds = 0
    #         species = "Red Flower"
    #         lifespan = 250
    #         nectar_regen = 3
    #         start = 10
    #         flower_nectar = 60
    #         occupied = False
    #         blocked_seeds = 0
    #         curr_flower = Flower(age, flower_seeds, lifespan, nectar_regen, 
    #                              start, flower_nectar, occupied, blocked_seeds)
    #         self.flowers.append(curr_flower)
    #     for i in range(20):
    #         age = 0
    #         flower_seeds = 0
    #         species = "Blue Flower"
    #         lifespan = 350
    #         nectar_regen = 3
    #         start = 10
    #         flower_nectar = 60
    #         occupied = False
    #         blocked_seeds = 0
    #         curr_flower = Flower(age, flower_seeds, lifespan, nectar_regen, 
    #                              start, flower_nectar, occupied, blocked_seeds)
    #         self.flowers.append(curr_flower)
    #     for i in range(20):
    #         age = 0
    #         flower_seeds = 0
    #         species = "Green Flower"
    #         lifespan = 300
    #         nectar_regen = 3
    #         start = 10
    #         flower_nectar = 60
    #         occupied = False
    #         blocked_seeds = 0
    #         curr_flower = Flower(age, flower_seeds, lifespan, nectar_regen, 
    #                              start, flower_nectar, occupied, blocked_seeds)
    #         self.flowers.append(curr_flower)
    #     for i in range(10):
    #         age = 0
    #         flower_seeds = 0
    #         species = "Invasive Flower"
    #         lifespan = 300
    #         nectar_regen = 6
    #         start = 10
    #         flower_nectar = 60
    #         occupied = False
    #         blocked_seeds = 0
    #         curr_flower = Flower(age, flower_seeds, lifespan, nectar_regen, 
    #                              start, flower_nectar, occupied, blocked_seeds)
    #         self.flowers.append(curr_flower)

    # def make_hives(self) -> None:
    #     for i in range(2):
    #         age = 0
    #         species = "Hives"
    #         producing_bees = False
    #         season_start = 0
    #         season_end = 1000
    #         storage_nectar = 0
    #         curr_hive = Hive(age, species, producing_bees, season_start, season_end, storage_nectar)
    #         self.hives.append(curr_hive)
        

    def make_seeds(self) -> None:
        for i in range(60):
            cur_flower = rand.randint(0, len(self.flowers) - 1)
            species = cur_flower.species()
            life_span = cur_flower.lifespan()
            start_of_bloom = cur_flower.start_of_bloom()
            occupied = cur_flower.occupied()
            nectar_regn = cur_flower.nectar_regeneration()
            active = False
            cur_seed = Seed(species, life_span, start_of_bloom, occupied, nectar_regn, active, cur_flower)
            self.seeds.append(cur_seed)
            

    def simulation() -> None:
        pass