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
        # Get bests individuals
        selected = self.selection(pop)
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