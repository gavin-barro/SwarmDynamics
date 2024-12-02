from datetime import timedelta

class Hive:
    '''
    producing-bees
    season-start
    season-end
    storage-nectar
    has-seed?
    '''

    def __init__(self, age: int, species: str, producing_bees: bool, season_start: timedelta, 
    season_end: timedelta, storage_nectar: int, has_seed: bool):
        self.age = age
        self.species = species
        self.producing_bees = producing_bees
        self.season_start = season_start
        self.season_end = season_end
        self.storage_nectar = storage_nectar
        self.has_seed = has_seed

    # Age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        self._age = value

    # Species
    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value: str):
        self._species = value

    # Producing Bees
    @property
    def producing_bees(self):
        return self._producing_bees

    @producing_bees.setter
    def producing_bees(self, value: bool):
        self._producing_bees = value

    # Season Start
    @property
    def season_start(self):
        return self._season_start

    @season_start.setter
    def season_start(self, value: timedelta):
        self._season_start = value

    # Season End
    @property
    def season_end(self):
        return self._season_end

    @season_end.setter
    def season_end(self, value: timedelta):
        self._season_end = value

    # Storage Nectar
    @property
    def storage_nectar(self):
        return self._storage_nectar

    @storage_nectar.setter
    def storage_nectar(self, value: int):
        self._storage_nectar = value

    # Has Seed
    @property
    def has_seed(self):
        return self._has_seed

    @has_seed.setter
    def has_seed(self, value: bool):
        self._has_seed = value
    
    