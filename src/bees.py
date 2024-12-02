from flowers import Flower
from hives import Hive

class Bee:
    MAX_NECTAR = 19

    def __init__(self, age: int, species: str, chosen_flower: Flower, previous_flower: Flower, 
                 destination: Flower, home_hive: Hive, collection_start_time: int, current_flower: Flower,  
                 count_carry_nectar: int, pollen: int):
        self._age = age
        self._species = species
        self._chosen_flower = chosen_flower
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
    def chosen_flower(self) -> Flower:
        return self._chosen_flower

    @chosen_flower.setter
    def chosen_flower(self, value: Flower) -> None:
        self._chosen_flower = value

    @property
    def previous_flower(self) -> Flower:
        return self._previous_flower

    @previous_flower.setter
    def previous_flower(self, value: Flower) -> None:
        self._previous_flower = value

    @property
    def destination(self) -> Flower:
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
    def current_flower(self) -> Flower:
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
        self._current_flower.produce_seeds()
        self._current_flower.age_flower()
        
    def move_bee(self) -> None:
        self._current_flower.occupied(False)
        self._previous_flower = self._current_flower
        self._current_flower = self._chosen_flower