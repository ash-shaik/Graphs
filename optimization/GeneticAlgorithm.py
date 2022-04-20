from numpy.random import randint


class EvolutionaryAlgorithm:
    def __init__(self, init_population, objective ,num_iterations):
        self.population = init_population
        self.max_iterations = num_iterations
        self.cost_function = objective
        self.units = {1: {'ATK': 100}
                      , 2: {'ATK': 600, 'BD': 0.50 # Boost BD by 50 percent for the current round
                            }
                      , 3: {'ATK': 700}
                      , 4: {'ATK': 400}
                      , 5: {'ATK': 400}
                      , 6: {'ATK': 1200, 'DEF': 150, 'BD': 0}}

    def fitness_function(self, individual):
        ## heart of a genetic algorithm
        ## determines how well it fulfills whatever criteria the algorithm is optimizing for
        # Final damage dealt to the monster after 4 rounds.
        """
         Damage = ATK * (100/ (DEF - BD) + 100)
        :param individual:
        :return:
        """
        for round in individual:
            unit = round[0]
            print(unit)

    def genetic_algorithm(self):
        # run each member of the population through a fitness function.
        for gen in range(self.max_iterations):
            self.cost_function(self.population[0])
            # select the fittest member of the population.


if __name__ == '__main__':
    population_size = 4

    population_ = [
          {1, 5, 2, 6}
        , {1, 2, 4, 3}
        , {4, 3, 6, 3}
        , {2, 4, 2, 4}
    ]
    # evAlgo = EvolutionaryAlgorithm(population_, 10)
    print(7000/15)
    ff = [450, 300, 200, 466.67]
    print("Fitness function for [1, 2, 4, 3] : {}".format(sum(ff)))

    print(7000/25)
    ff = [200, 466.67, 600, 280]
    print("Fitness function for [4, 3, 6, 3] : {}".format(sum(ff)))

    ff = [450, 235.29, 387.10, 600]
    print("Fitness function for [1, 5, 2, 6] : {}".format(sum(ff)))

    ff = [300, 200, 480, 200]
    print("Fitness function for [2, 4, 2, 4] : {}".format(sum(ff)))

    print(4000/17)
    ff = [450, 235.29, 545.45, 350]
    print("Fitness function for [1, 5, 6, 3] : {}".format(sum(ff)))

    ff = [200, 466.67, 300, 600]
    print("Fitness function for [4, 3, 2, 6] : {}".format(sum(ff)))

    ff = [450, 300, 300, 200]
    print("Fitness function for [1, 2, 2, 4] : {}".format(sum(ff)))

    ff = [300, 200, 266.67, 350]
    print("Fitness function for [2, 4, 4, 3] : {}".format(sum(ff)))

    print(4000/25)
    ff = [600, 160, 450, 280]
    print("Fitness function for [6, 5, 1, 3] : {}".format(sum(ff)))

    ff = [200, 720, 300, 350]
    print("Fitness function for [4, 2, 2, 3] : {}".format(sum(ff)))
