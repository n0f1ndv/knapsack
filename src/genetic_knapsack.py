import random

from generate_data import read_data_json

# TODO: Fix bug with calculating data["penalties"]
def genetic_knapsack(data, settings):
    def calculate_fitness(individual, values, weights, capacity, categories, penalties):
        total_value = sum(data["values"][i] for i in range(len(individual)) if individual[i] == 1)
        total_weight = sum(data["weights"][i] for i in range(len(individual)) if individual[i] == 1)

        if total_weight > data["capacity"]:
            return 0

        total_penalty = 0
        for i in range(len(individual) - 1):
            if individual[i] == 1 and individual[i + 1] == 1 and data["categories"][i] != data["categories"][i + 1]:
                key = f"{data["categories"][i]}{data["categories"][i + 1]}"
                total_penalty += data["penalties"].get(key, 0)

        return total_value - total_penalty

    population = [[random.randint(0, 1) for _ in range(data["items_number"])] for _ in range(settings["population"])]

    for generation in range(settings["generations"]):
        fitness_scores = [calculate_fitness(individual, data["values"], data["weights"], data["capacity"], data["categories"], data["penalties"]) for individual in population]

        selected = []
        for _ in range(settings["population"]):
            tournament = random.sample(range(settings["population"]), settings["to_sample"])
            selected.append(population[max(tournament, key=lambda i: fitness_scores[i])])

        next_population = []
        for i in range(0, settings["population"], 2):
            if i + 1 < settings["population"]:
                crossover_point = random.randint(1, data["items_number"] - 1)
                offspring1 = selected[i][:crossover_point] + selected[i + 1][crossover_point:]
                offspring2 = selected[i + 1][:crossover_point] + selected[i][crossover_point:]
                next_population.append(offspring1)
                next_population.append(offspring2)
            else:
                next_population.append(selected[i])

        for individual in next_population:
            for j in range(data["items_number"]):
                if random.random() < settings["mutations"]:
                    individual[j] = 1 - individual[j]

        population = next_population

    fitness_scores = [calculate_fitness(individual, data["values"], data["weights"], data["capacity"], data["categories"], data["penalties"]) for individual in population]
    best_index = max(range(settings["population"]), key=lambda i: fitness_scores[i])
    best_individual = population[best_index]
    
    total_value = sum(data["values"][i] for i in range(data["items_number"]) if best_individual[i] == 1)
    total_weight = sum(data["weights"][i] for i in range(data["items_number"]) if best_individual[i] == 1)
    total_penalty = 0

    for i in range(data["items_number"] - 1):
        if best_individual[i] == 1 and best_individual[i + 1] == 1 and data["categories"][i] != data["categories"][i + 1]:
            key = f"{data["categories"][i]}{data["categories"][i + 1]}"
            total_penalty += data["penalties"].get(key, 0)
