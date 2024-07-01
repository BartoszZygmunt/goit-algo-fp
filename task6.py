items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    """
    Implements the greedy algorithm to maximize the ratio of calories to cost within the budget.
    """
    # Sort items by calories to cost ratio in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(item)
            total_cost += details["cost"]
            total_calories += details["calories"]
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    """
    Implements the dynamic programming algorithm to maximize total calories within the budget.
    """
    n = len(items)
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]
    
    # Create a 2D DP array with dimensions (n+1) x (budget+1)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find the items included in the optimal solution
    selected_items = []
    total_cost = 0
    total_calories = 0
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            total_cost += costs[i - 1]
            total_calories += calories[i - 1]
            w -= costs[i - 1]
    
    return selected_items, total_cost, total_calories

# Test
if __name__ == "__main__":
    budget = 100
    
    print("Greedy Algorithm Selection:")
    selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    print(f"Selected items: {selected_items_greedy}")
    print(f"Total cost: {total_cost_greedy}, Total calories: {total_calories_greedy}, Budget: {budget}")
    
    print("\nDynamic Programming Selection:")
    selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
    print(f"Selected items: {selected_items_dp}")
    print(f"Total cost: {total_cost_dp}, Total calories: {total_calories_dp}, Budget: {budget}")
