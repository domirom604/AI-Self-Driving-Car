import keras
import main
from KerasGA import GeneticAlgorithm

def model():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(3,activation='relu',input_shape=(3,)))
    model.add(keras.layers.Dense(5, activation='relu'))
    model.add(keras.layers.Dense(2, activation='sigmoid'))
    return model


scores = []
population_size =  10
model = model()
GA = GeneticAlgorithm(model, population_size = population_size, selection_rate = 0.1, mutation_rate = 0.2)
population = GA.initial_population()

while 1:
    for chromosome in population:
        model.set_weights(chromosome)
        game = main.Play(model=model,control='keras')
        score = game.run()
        scores.append(score)


    # Selection:
    # 'scores' is a list of length = population_size
    # 'top_performers' is a list of tuples: (chromosome, it's score)
    top_performers = GA.strongest_parents(population,scores)

    # Make pairs:
    # 'GA.pair' return a tuple of type: (chromosome, it's score)
    pairs = []
    while len(pairs) != GA.population_size:
        pairs.append(GA.pair(top_performers))

    # Crossover:
    base_offsprings =  []
    for pair in pairs:
        offsprings = GA.crossover(pair[0][0], pair[1][0])
        # 'offsprings' contains two chromosomes
        base_offsprings.append(offsprings[-1])

    # Mutation:
    population = GA.mutation(base_offsprings)