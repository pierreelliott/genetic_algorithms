from cross_overs import CrossOverRandomSliceTwo, CrossOverRandomTwo
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
    cross_over = CrossOverRandomSliceTwo(0.6)
    mutation = NCharSeqNextPrevMutation(n=2)
    exploration = SimpleExploration(cross_over, mutation, elite_size=int(population_size / 10))

    population = Population(population_size, exploration=exploration)
    averages, bests, best = evolve_population(population, max_epochs=epochs, show_progress=False)
    print(f"Best solution found: {best.phenotype()} ({best.score})")
    plot_results(averages, bests)


def stats(configs, nb_repeats):
    to_plot = []
    for i, conf in enumerate(configs):
        print(i, conf)
        repeats = []
        for i in range(nb_repeats):
            exploration = SimpleExploration(conf['cross_over'],
                                            conf['mutation'],
                                            elite_size=conf['population_size'] // 10)
            population = Population(conf['population_size'], exploration=exploration)
            _, bests, _ = evolve_population(population, max_epochs=conf['epochs'], show_progress=False)
            repeats.append(bests)
        average = []
        for i in range(conf['epochs']):
            s = 0
            for r in repeats:
                s += r[i]
            average.append(s/nb_repeats)
        to_plot.append(average)

    for i, l in enumerate(to_plot):
        plt.plot(l, label=str(i))
    plt.xlabel('Itérations')
    plt.ylabel('Scores')
    plt.legend(loc="lower right")
    plt.show()


configs = [
    {
        'population_size': 200,
        'epochs': 200,
        'mutation': NCharSeqNextPrevMutation(n=2),
        'cross_over': CrossOverRandomTwo(1.0),
    },
    {
        'population_size': 200,
        'epochs': 200,
        'mutation': NCharSeqNextPrevMutation(n=2),
        'cross_over': CrossOverRandomSliceTwo(1.0),
    }
]

stats(configs, nb_repeats=25)
# search(population_size=200, epochs=100)
