import random
from utils import copy_individual
from population import generate_population, Individual


class RandomExploration:
    def evolve(self, pop):
        pop.population = generate_population(len(pop.population))


class SimpleExploration:
    def __init__(self, cross_over, mutation, elite_size=5):
        self.cross_over = cross_over
        self.mutate = mutation
        self.elite_size = elite_size

    def evolve(self, pop):
        new_population = []
        # Get bests individuals...
        selected = self.selection(pop)
        # ... and keep them
        new_population.extend(selected)
        # Do mutations for the rest of the population
        for i in range(pop.size - self.elite_size):
            individual = Individual([])
            while not 12 < len(individual.phenotype()) < 18:
                if random.random() < self.cross_over.prob:
                    individual = self.cross_over(selected)
                else:
                    individual = selected[0].clone()
    
                self.mutate(individual)  # In-place
            new_population.append(individual)
        pop.population = new_population

    def selection(self, pop):
        return pop.population[:self.elite_size]
    

class TerraExploration:
    """
    Mimick the existence of continents by evolving the population in small groups and reuniting them once in a while
    """
    def __init__(self, cross_over, mutation, pop_size, elite_size=5, continents, reunion):
        self.cross_over = cross_over
        self.mutate = mutation
        self.elite_size = elite_size
        self.size = pop_size
        self.epoch = 0
        self.reunion = reunion
        self.continents = []
        
        # continents is a tuple like (0.3, 0.2, 0.5) -> 3 continents with 30%, 20% and 50% of total population
        for cont in continents:
            self.continents.append(int(pop_size * cont))
        self.continents[-1] = pop_size  # To correct rounding errors
        
    def evolve(self, pop):
        new_population = []
        if self.epoch % self.reunion == 0:  # Reproduction of the entire population
            new_population.extend(self.populate(pop.population, 0, self.size))
        else:  # Reproduction of population in small groups
            start = 0
            for continent in self.continents:
                new_population.extend(self.populate(pop.population, start, continent))
                start = continent
        pop.population = new_population
        self.epoch += 1
                
        
    def selection(self, population):
        return population[:self.elite_size]
    
    def populate(self, population, start, end):
        pop = population.population[start:end]  # Select population of specific "continent"
        selected = self.selection(pop)  # Select bests individuals in the population
        
        pop_size = len(pop)  # To keep same number of individuals
        new_pop = []
        while len(new_pop) != pop_size:
            individual = Individual([])
            while not 12 < len(individual.phenotype()) < 18:
                if random.random() < self.cross_over.prob:
                    individual = self.cross_over(selected)
                else:
                    individual = selected[0].clone()
    
                self.mutate(individual)  # In-place
            new_pop.append(individual)
        return new_pop