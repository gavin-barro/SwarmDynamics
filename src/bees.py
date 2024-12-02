class Bee:
    
    def __init__(self, age: int, species: str, chosen_flower, chosen_patch, previous_flower, destination, home_hive,
                    collection_start_time, current_flower,  count_carry_nectar, pollen):
        self._age = age
        self._species = species
        self._chosen_flower = chosen_flower
        self._chosen_patch = chosen_patch
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
    def age(self, value: int):
        self._age = value  
        
    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value

    @property
    def chosen_flower(self):
        return self._chosen_flower

    @chosen_flower.setter
    def chosen_flower(self, value):
        self._chosen_flower = value

    @property
    def chosen_patch(self):
        return self._chosen_patch

    @chosen_patch.setter
    def chosen_patch(self, value):
        self._chosen_patch = value

    @property
    def previous_flower(self):
        return self._previous_flower

    @previous_flower.setter
    def previous_flower(self, value):
        self._previous_flower = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value

    @property
    def home_hive(self):
        return self._home_hive

    @home_hive.setter
    def home_hive(self, value):
        self._home_hive = value

    @property
    def collection_start_time(self):
        return self._collection_start_time

    @collection_start_time.setter
    def collection_start_time(self, value):
        self._collection_start_time = value

    @property
    def current_flower(self):
        return self._current_flower

    @current_flower.setter
    def current_flower(self, value):
        self._current_flower = value

    @property
    def count_carry_nectar(self):
        return self._count_carry_nectar

    @count_carry_nectar.setter
    def count_carry_nectar(self, value):
        self._count_carry_nectar = value

    @property
    def pollen(self):
        return self._pollen

    @pollen.setter
    def pollen(self, value):
        self._pollen = value  