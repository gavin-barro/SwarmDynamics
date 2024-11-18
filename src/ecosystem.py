from species import Species
import random

class Ecosystem:
    """
    
        TODO: Add a decription
    """
    
    
    def __init__(self, initial_resources: int, resource_regeneration_rate: float = 0.1):
        self.initial_resources = initial_resources
        self.resource_regeneration_rate = resource_regeneration_rate
        self.species_list = []
        
    
    def add_species(self, species: Species) -> None:
        """Adds a species to the ecosystem."""
        self.species_list.append(species)
        
    def remove_species(self, speices: Species) -> None:
        """Removes a species to the ecosystem."""
        self.species_list.remove(speices)
        
