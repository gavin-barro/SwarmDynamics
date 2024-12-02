class Bee:
    
    def __init__(self, age: int, species: str, chosen_flower, chosen_patch, previous_flower, destination, home_hive,
                    collection_start_time, current_flower,  count_carry_nectar, pollen):
        self.age = age
        self.species = species
        self.chosen_flower = chosen_flower
        self.chosen_patch = chosen_patch
        self.previous_flower = previous_flower
        self.destination = destination
        self.home_hive = home_hive
        self.collection_start_time = collection_start_time
        self.current_flower = current_flower
        self.count_carry_nectar = count_carry_nectar
        self.pollen = pollen