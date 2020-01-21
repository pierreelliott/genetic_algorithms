import random
from utils import copy_individual
from population import generate_population


class RandomExploration:
    def evolve(self, pop):
        pop.population = generate_population(len(pop.population))


class SimpleExploration:
    def __init__(self, cross_over, mutation, bests_size=5):
        self.cross_over = cross_over
        self.mutate = mutation
        self.bests_size = bests_size

    def evolve(self, pop):
        new_population = []
        # Get bests individuals
        selected = self.selection(pop)
        # Do mutations for the rest of the population
        for i in range(pop.size - self.bests_size):  ########################## FIXME Gérer les individus "mort-nés"
            if random.random() < self.cross_over.prob:
                individual = self.cross_over(selected)
            else:
                individual = selected[0].clone()  ############################################# FIXME

            self.mutate(individual)  # In-place
            new_population.append(individual)
        pop.population = new_population

    def selection(self, pop):
        return pop.population[:self.bests_size]