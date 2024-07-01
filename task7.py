import random
import matplotlib.pyplot as plt

# Simulates rolling two six-sided dice and returns the result as a tuple.
def roll_dice():  
    return random.randint(1, 6), random.randint(1, 6)



# Simulates a given number of dice rolls and counts the occurrences of each possible sum (2 to 12).
def simulate_dice_rolls(num_rolls):
    
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        die1, die2 = roll_dice()
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1
    
    return sum_counts

# Calculates the probabilities of each sum based on the number of occurrences.
def calculate_probabilities(sum_counts, num_rolls):
    
    probabilities = {sum_val: (count / num_rolls) * 100 for sum_val, count in sum_counts.items()}
    return probabilities

# Plots the probabilities of each sum and optionally compares with theoretical probabilities.
def plot_probabilities(probabilities, theoretical_probabilities=None):
    
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, tick_label=sums, color='skyblue', label='Monte Carlo Simulation')
    
    if theoretical_probabilities:
        theoretical_probs = [theoretical_probabilities[sum_val] for sum_val in sums]
        plt.plot(sums, theoretical_probs, color='red', marker='o', linestyle='dashed', label='Theoretical Probability')
    
    plt.xlabel('Sum')
    plt.ylabel('Probability (%)')
    plt.title('Probability of Sums when Throwing Two Dice')
    plt.legend()
    plt.show()

# Returns the theoretical probabilities of each sum when throwing two dice.
def theoretical_probabilities():
    
    return {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78
    }

# Compares the simulated probabilities with the theoretical probabilities and prints the comparison.
def compare_probabilities(simulated_probs, theoretical_probs):
    
    print(f"{'Sum':<5} {'Simulated Probability (%)':<25} {'Theoretical Probability (%)':<25} {'Difference (%)'}")
    for sum_val in sorted(simulated_probs.keys()):
        simulated = simulated_probs[sum_val]
        theoretical = theoretical_probs[sum_val]
        difference = simulated - theoretical
        print(f"{sum_val:<5} {simulated:<25.2f} {theoretical:<25.2f} {difference:.2f}")

def main():
    num_rolls = 1000000  # Number of dice rolls for the simulation
    sum_counts = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(sum_counts, num_rolls)
    
    # Display the results in a table format
    print(f"{'Sum':<5} {'Count':<10} {'Probability (%)'}")
    for sum_val in sorted(probabilities.keys()):
        print(f"{sum_val:<5} {sum_counts[sum_val]:<10} {probabilities[sum_val]:.2f}%")
    
    # Theoretical probabilities
    theoretical_probs = theoretical_probabilities()
    
    # Plot the probabilities
    plot_probabilities(probabilities, theoretical_probs)
    
    # Compare simulated probabilities with theoretical probabilities
    compare_probabilities(probabilities, theoretical_probs)

if __name__ == "__main__":
    main()
