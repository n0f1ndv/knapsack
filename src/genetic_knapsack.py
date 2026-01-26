"""
@file genetic_knapsack.py
@brief Provides genetic algorithm for an instance of a problem (with greedy repair)
"""
import random
import time

from generate_data import read_data_json
from calculate_penalty import calculate_penalty
from minimize_penalty import minimize_penalty

def greedy_repair(individual, data):
    """
    @brief Repair binary individual to be feasible by removing items until weight is less than capacity.
    @param individual (list): Binary list of used elements
    @param data (dict): Instance of a problem read from json
    """
    weights = data["weights"]
    values = data["values"]
    capacity = data["capacity"]

    total_weight = sum(w for i, w in enumerate(weights) if individual[i] == 1)
    if total_weight <= capacity:
        return individual

    used = [(((values[i] / weights[i]) if weights[i] > 0 else float('inf')), i)
            for i in range(len(individual)) if individual[i] == 1]

    used.sort()

    for _, idx in used:
        if total_weight <= capacity:
            break
        individual[idx] = 0
        total_weight -= weights[idx]

    return individual

def genetic_knapsack(data, settings, minimize=False):
    """
    @brief Genetic algorithm 
    @param data (dict): Instance of a problem read from json
    @param settings (dict): Settings of genetic algorithm read from json
    @param minimize (bool): Decides whether to call minimize_penalty()
    """
    def calculate_solution(individual, data, fitness, minimize=False):
        """
        @brief Helper function that calculates final solution or fitness of an individual
        @param individual (list): Binary list of used elements
        @param data (dict): Instance of a problem read from json
        @param fitness (bool): Decides upon return type. True for calculating fitness, False for final solution
        @param minimize (bool): Decides whether to call minimize_penalty()
        """
        total_value = sum(data["values"][i] for i in range(len(individual)) if individual[i] == 1)
        total_weight = sum(data["weights"][i] for i in range(len(individual)) if individual[i] == 1)

        if fitness is True and total_weight > data["capacity"]:
            return float("-inf")

        used_elements_indices = [i for i in range(len(individual)) if individual[i] == 1]

        if minimize and used_elements_indices:
            used_elements_indices = minimize_penalty(data, used_elements_indices)

        total_penalty = calculate_penalty(data, used_elements_indices)

        if fitness:
            return total_value - total_penalty
        else:
            return total_value, total_weight, total_penalty, total_value - total_penalty

    def random_feasible_individual(data):
        ind = [0] * data["items_number"]
        indices = list(range(data["items_number"]))
        random.shuffle(indices)
        current_weight = 0
        for i in indices:
            w = data["weights"][i]
            if current_weight + w <= data["capacity"]:
                if random.random() < 0.5:
                    ind[i] = 1
                    current_weight += w
        return ind

    population = [random_feasible_individual(data) for _ in range(settings["population"])]

    for generation in range(settings["generations"]):
        fitness_scores = [calculate_solution(individual, data, True, minimize) for individual in population]

        selected = []
        for _ in range(settings["population"]):
            tournament = random.sample(range(settings["population"]), settings["to_sample"])
            winner_idx = max(tournament, key=lambda i: fitness_scores[i])
            selected.append(population[winner_idx][:])

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

            if sum(data["weights"][i] for i in range(data["items_number"]) if individual[i] == 1) > data["capacity"]:
                greedy_repair(individual, data)

            if minimize:
                used = [i for i in range(len(individual)) if individual[i] == 1]
                if used:
                    kept = minimize_penalty(data, used)
                    new_ind = [1 if idx in kept else 0 for idx in range(data["items_number"])]
                    individual[:] = new_ind
                    if sum(data["weights"][i] for i in range(data["items_number"]) if individual[i] == 1) > data["capacity"]:
                        greedy_repair(individual, data)

        population = next_population

    fitness_scores = [calculate_solution(individual, data, True, minimize) for individual in population]
    best_index = max(range(settings["population"]), key=lambda i: fitness_scores[i])

    best_individual = population[best_index]

    return *calculate_solution(best_individual, data, False, minimize), best_individual
