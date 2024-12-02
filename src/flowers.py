from datetime import timedelta
from seeds import Seed

class Flower:
    
    MAX_AGE: int = 20
    
    def __init__(self, age: int, species: str, flower_seeds: int, lifespan: int, 
                 nectar_regeneration:float, start_of_bloom: int, flower_nectar: float, occupied: bool, 
                 blocked_seeds: list[Seed]):
        self._age = age
        self._species = species
        self._flower_seeds = flower_seeds
        self._lifespan = lifespan
        self._nectar_regeneration = nectar_regeneration
        self._start_of_bloom = start_of_bloom
        self._flower_nectar = flower_nectar
        self._occupied = occupied
        self._blocked_seeds = blocked_seeds
        
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

    # Blocked Seeds
    @property
    def blocked_seeds(self) -> list[Seed]:
        return self._blocked_seeds

    @blocked_seeds.setter
    def blocked_seeds(self, value: Seed) -> None:
        self._blocked_seeds.append(value)
    
    def update_flower(self, value: int) -> int:
        self.occupied = True
        curr_flower_nectar = self._flower_nectar - value + self._nectar_regeneration
        if curr_flower_nectar > 0:
            self._flower_nectar = curr_flower_nectar
        else:
            value = self._flower_nectar
            self._flower_nectar = 0
        return value
    
    def produce_seeds(self):
        """Flower produces seeds if pollinated."""
        if self.occupied:
            # Seed production logic here, for simplicity assume 1 seed per tick
            self.flower_seeds += 1
            new_seed = Seed(age=0, species=self.species, lifespan=10, 
                            start_of_bloom=self._start_of_bloom, occupied=False, 
                            nectar_regeneration=self._nectar_regeneration, active=True)
            self.blocked_seeds(new_seed)
            self.occupied = False  # Reset after seed production
            return True
        return False

    def age_flower(self):
        """Aging the flower over time."""
        self.age += 1
        if self.age > self.lifespan:
            return False  # Flower dies after reaching lifespan
        return True

        