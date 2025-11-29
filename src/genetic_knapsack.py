import random

from generate_data import read_data_json

def calculate_fitness(individual, values, weights, capacity, categories, penalties):
    total_value = sum(values[i] for i in range(len(individual)) if individual[i] == 1)
    total_weight = sum(weights[i] for i in range(len(individual)) if individual[i] == 1)

    if total_weight > capacity:
        return 0

    total_penalty = 0
    for i in range(len(individual) - 1):
        if individual[i] == 1 and individual[i + 1] == 1 and categories[i] != categories[i + 1]:
            key = f"{categories[i]}{categories[i + 1]}"
            total_penalty += penalties.get(key, 0)

    return total_value - total_penalty

def genetic_knapsack(path_to_file):
    print("!!! Solving using genetic algorithm")

    data = read_data_json(path_to_file)    
    items_number = data["items_number"]
    values = data["values"]
    weights = data["weights"]
    capacity = data["capacity"]
    categories = data["categories"]
    penalties = data["penalties"]

    population_size = int(input("population_size>")) # 100
    generations = int(input("generations> ")) # 100
    mutation_rate = float(input("mutation_rate")) # 0.01

    population = [[random.randint(0, 1) for _ in range(items_number)] for _ in range(population_size)]

    for generation in range(generations):
        fitness_scores = [calculate_fitness(i, values, weights, capacity, categories, penalties) for i in population]

        selected = []
        for _ in range(population_size):
            tournament = random.sample(range(population_size), 5)
            selected.append(population[max(tournament, key=lambda i: fitness_scores[i])])

        next_population = []
        for i in range(0, population_size, 2):
            if i + 1 < population_size:
                crossover_point = random.randint(1, items_number - 1)
                offspring1 = selected[i][:crossover_point] + selected[i + 1][crossover_point:]
                offspring2 = selected[i + 1][:crossover_point] + selected[i][crossover_point:]
                next_population.extend([offspring1, offspring2])
            else:
                next_population.append(selected[i])

        for ind in next_population:
            for j in range(items_number):
                if random.random() < mutation_rate:
                    ind[j] = 1 - ind[j]

        population = next_population

    fitness_scores = [calculate_fitness(ind, values, weights, capacity, categories, penalties) for ind in population]
    best_index = max(range(population_size), key=lambda i: fitness_scores[i])

    print(fitness_scores)
    print(best_index)
