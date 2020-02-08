from cross_overs import CrossOverRandomSliceTwo, CrossOverScoreSliceTwo
from explorations import SimpleExploration
from mutations import NCharRandomMutation, NCharNextPrevMutation, NCharSeqMutation, NCharSeqNextPrevMutation
from population import Population
from matplotlib import pyplot as plt


def plot_results(average, bests):
    plt.plot(average, color='green', linestyle='dotted', label='Moyenne de la population actuelle')
    plt.plot(bests, color='red', label='Maximum trouvé')
    plt.xlabel('Itérations')
    plt.ylabel('Scores')
    plt.legend(loc="lower right")
    plt.show()


def evolve_population(population, max_epochs=1000, show_progress=False, progress_step=10):
    averages = []
    bests = []
    best = population.population[0]
    for epoch in range(max_epochs):
        population.evaluate()
        b = population.get_max()
        best = b if b.score > best.score else best
        bests.append(best.score)
        average = population.get_average_score()
        averages.append(average)

        if show_progress:
            print(f"Epoch {epoch + 1}/{max_epochs}: Best {best.phenotype()} ({best.score}) (average: {average})")

        if best.score == 1.0:
            print(f"Best found: {best.phenotype()} at Epoch {epoch + 1}/{max_epochs}!")
            break

        population.evolve()
    return averages, bests, best


def search(population_size=10, epochs=10):
    cross_over = CrossOverScoreSliceTwo(0.6)
    mutation = NCharSeqNextPrevMutation(n=2)
    exploration = SimpleExploration(cross_over, mutation, elite_size=int(population_size / 10))

    population = Population(population_size, exploration=exploration)
    averages, bests, best = evolve_population(population, max_epochs=epochs, show_progress=False)
    print(f"Best solution found: {best.phenotype()} ({best.score})")
    plot_results(averages, bests)


search(population_size=200, epochs=100)
