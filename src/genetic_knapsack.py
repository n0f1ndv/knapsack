import random

from generate_data import read_data_json
from calculate_penalty import calculate_penalty
from minimize_penalty import minimize_penalty

# FIXED BUGS BUT STILL...
# TESTING IN PROGRESS

def genetic_knapsack(data, settings, minimize=False):
    def calculate_solution(individual, data, fitness=True, minimize=False):
        total_value = sum(data["values"][i] for i in range(len(individual)) if individual[i] == 1)
        total_weight = sum(data["weights"][i] for i in range(len(individual)) if individual[i] == 1)

        if total_weight > data["capacity"]:
            return 0

        used_elements_indices = [i for i in range(len(individual)) if individual[i] == 1]

        if (minimize and len(used_elements_indices)):
            used_elements_indices = minimize_penalty(data, used_elements_indices)

        total_penalty = calculate_penalty(data, used_elements_indices)

        if (fitness):
            return total_value - total_penalty
        else:
            return total_value, total_weight, total_penalty, total_value - total_penalty

    population = [[random.randint(0, 1) for _ in range(data["items_number"])] for _ in range(settings["population"])]

    for generation in range(settings["generations"]):
        fitness_scores = [calculate_solution(individual, data, True, minimize) for individual in population]

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

    fitness_scores = [calculate_solution(individual, data, True, minimize) for individual in population]
    best_index = max(range(settings["population"]), key=lambda i: fitness_scores[i])
    best_individual = population[best_index]  

    return *calculate_solution(best_individual, data, False, minimize), best_individual
