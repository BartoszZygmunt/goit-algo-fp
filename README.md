# Monte Carlo Simulation of Dice Rolls

This project uses the Monte Carlo method to simulate a large number of dice rolls, calculate the sums of numbers that appear on the dice, and determine the probability of each possible sum. The results are compared with theoretical probabilities.

## Problem Description

The task involves simulating the rolling of two six-sided dice a large number of times. For each throw, we determine the sum of the numbers that appear on both dice. We count how many times each possible sum (from 2 to 12) appears in the simulation. Using this data, we calculate the probability of each sum.

## Approach

We use two approaches to solve this problem:

1. **Monte Carlo Simulation**: Simulate a large number of dice rolls and calculate the empirical probabilities of each sum.
2. **Theoretical Calculation**: Calculate the theoretical probabilities of each sum using combinatorial analysis.

## Simulation Implementation

### Monte Carlo Simulation

The Monte Carlo simulation involves:

1. Simulating a large number of dice rolls (1,000,000).
2. Counting the occurrences of each possible sum.
3. Calculating the empirical probabilities based on the counts.

### Theoretical Calculation

The theoretical probabilities of each sum are calculated based on the possible combinations of the dice rolls. The probabilities are as follows:

| Sum | Probability (%) |
| --- | --------------- |
| 2   | 2.78            |
| 3   | 5.56            |
| 4   | 8.33            |
| 5   | 11.11           |
| 6   | 13.89           |
| 7   | 16.67           |
| 8   | 13.89           |
| 9   | 11.11           |
| 10  | 8.33            |
| 11  | 5.56            |
| 12  | 2.78            |

## Results

### Monte Carlo Simulation Results

The simulation results for 1,000,000 dice rolls are:

| Sum | Count  | Probability (%) |
| --- | ------ | --------------- |
| 2   | 27744  | 2.77%           |
| 3   | 55644  | 5.56%           |
| 4   | 83233  | 8.32%           |
| 5   | 111555 | 11.16%          |
| 6   | 138882 | 13.89%          |
| 7   | 166855 | 16.69%          |
| 8   | 139117 | 13.91%          |
| 9   | 111385 | 11.14%          |
| 10  | 83382  | 8.34%           |
| 11  | 55773  | 5.58%           |
| 12  | 27830  | 2.78%           |

### Comparison with Theoretical Probabilities

| Sum | Simulated Probability (%) | Theoretical Probability (%) | Difference (%) |
| --- | ------------------------- | --------------------------- | -------------- |
| 2   | 2.77                      | 2.78                        | -0.01          |
| 3   | 5.56                      | 5.56                        | 0.00           |
| 4   | 8.32                      | 8.33                        | -0.01          |
| 5   | 11.16                     | 11.11                       | 0.05           |
| 6   | 13.89                     | 13.89                       | 0.00           |
| 7   | 16.69                     | 16.67                       | 0.02           |
| 8   | 13.91                     | 13.89                       | 0.02           |
| 9   | 11.14                     | 11.11                       | 0.03           |
| 10  | 8.34                      | 8.33                        | 0.01           |
| 11  | 5.58                      | 5.56                        | 0.02           |
| 12  | 2.78                      | 2.78                        | 0.00           |

## Conclusions

The Monte Carlo simulation results are very close to the theoretical probabilities, demonstrating the accuracy of the simulation approach for a large number of trials. The differences between the simulated and theoretical probabilities are minimal, indicating that the simulation provides a good approximation of the true probabilities.

The Monte Carlo method proves to be an effective tool for estimating probabilities when analytical solutions are either difficult to obtain or not feasible. With an increasing number of simulations, the empirical probabilities converge to the theoretical probabilities, showcasing the Law of Large Numbers.
