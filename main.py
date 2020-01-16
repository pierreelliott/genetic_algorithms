from cross_overs import CrossOverRandomTwo
from explorations import SimpleExploration
from mutations import NCharMutation
from population import Population
from matplotlib import pyplot as plt


def plot_results(average, bests):
    plt.plot(average, color='green', linestyle='dotted', label='Moyenne de la population actuelle')
    plt.plot(bests, color='red', label='Maximum trouvé')
    plt.xlabel('Itérations')
    plt.ylabel('Scores')
    plt.legend(loc="lower right")
    plt.show()


def evolve(pop, epochs=5, show_progress=False):
    averages = []
    bests = []
    best = pop.population[0]
    for epoch in range(epochs):
        pop.evaluate()
        b = max(pop.population, key=lambda x: x['score'])
        best = b if b['score'] > best['score'] else best
        bests.append(best['score'])
        average = sum(map(lambda x: x['score'], pop.population)) / pop.size
        averages.append(average)
        if show_progress:
            print(f"Epoch {epoch+1}/{epochs}: Best {''.join(best['genotype'])} ({best['score']}) (average: {average})")
#             print(str(pop))
        if best['score'] == 1.0:
            print(f"Best found: {''.join(best['genotype'])} at Epoch {epoch+1}/{epochs}!")
            break
        pop.evolve()
    return averages, bests, best


def search(population_size=10, epochs=10):
    cross_over = CrossOverRandomTwo(0.6)
    mutation = NCharMutation(n=2)
    exploration = SimpleExploration(cross_over, mutation)

    population = Population(population_size, exploration=exploration)
    averages, bests, best = evolve(population, epochs=epochs, show_progress=False)
    print(f"Best solution found: {''.join(best['genotype'])} ({best['score']})")
    plot_results(averages, bests)


search(population_size=200, epochs=100)
