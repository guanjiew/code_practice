# Given a dataset of coal mining data, which contains the following fields:
# 1. Coal name
# 2. Coal mining quantity
# 3. Coal mining price
# 4. Coal mining profit
# 5. Coal mining loss
# 6. Coal production capacity
# 7. Coal power plant capacity
# 8. Coal plutonic rock content

# Given a set of constraints, write a program to find the optimal mixture of coal to
# mining price.
# 1. The optimal mixture should be the one that maximizes the profit.
# 2. The profit is the difference between the mining price and the cost of the coal.
# 3. The cost of the coal is the sum of the coal mining quantity times the coal mining price.
# 4. The profit is the difference between the mining price and the cost of the coal.


import matplotlib.pyplot as plt
import numpy as np
# read the data in csv file and store it in a panda dataframe
import pandas as pd
import seaborn as sns


def read_data(file_name):
    df = pd.read_csv(file_name)
    return df


# plot the data
def plot_data(df):
    sns.pairplot(df, hue='Coal Name')
    plt.show()


# calculate the profit of each coal
def calculate_profit(df):
    df['Profit'] = df['Mining Price'] - df['Coal Mining Cost']
    return df


# calculate the cost of each coal
def calculate_cost(df):
    df['Coal Mining Cost'] = df['Coal Mining Quantity'] * df['Coal Mining Price']
    return df


# read in the constraints and use Simplex algorithm to solve the optimization problem
def solve_optimization_problem(df, constraints):
    # Read in the constraints
    A = np.array(constraints['A'])
    b = np.array(constraints['b'])
    c = np.array(constraints['c'])

    # Initialize the simplex tableau
    m = len(A[0])
    n = len(A)
    tableau = np.zeros((m + 1, n + m + 1))
    for i in range(n):
        tableau[i, i] = 1
    for i in range(n, n + m):
        tableau[i, i] = -1
    for i in range(n + m, n + m + 1):
        tableau[i, i] = 1

    # Initialize the basis  
    basis = []
    for i in range(n):
        basis.append(i)
    basis.append(n + m)
    basis.append(n + m + 1)

    # Initialize the objective function
    c_prime = np.zeros(m + 1)
    c_prime[m] = 1
    c_prime[m + 1] = -1
    c_prime[m + 2] = 0

    # Solve the optimization problem
    while True:
        # Find the pivot column
        pivot_col = -1
        for j in range(n + m + 1):
            if c_prime[j] > 0:
                pivot_col = j
                break
        if pivot_col == -1:
            break

        # Find the pivot row
        pivot_row = -1
        for i in range(n):
            if tableau[i, pivot_col] > 0:
                pivot_row = i
                break
        if pivot_row == -1:
            break

        # Update the basis
        basis[pivot_row] = pivot_col

        # Update the simplex tableau
        for i in range(n + m + 1):
            if i != pivot_col:
                tableau[pivot_row, i] = tableau[pivot_row, i] / tableau[pivot_row, pivot_col]
        for i in range(n + m + 1):
            if i != pivot_col:
                tableau[i, pivot_col] = tableau[i, pivot_col] / tableau[pivot_row, pivot_col]
        tableau[pivot_row, pivot_col] = 1

        # Update the objective function
        for i in range(n + m + 1):
            c_prime[i] = c_prime[i] - tableau[pivot_row, i] * c_prime[pivot_col]

    # Find the optimal solution
    x = np.zeros(n)
    for i in range(n):
        x[i] = tableau[i, n + m + 1]
    return x


# calculate the optimal solution
def calculate_optimal_solution(df, x):
    df['Optimal Solution'] = x
    return df


# calculate the optimal profit
def calculate_optimal_profit(df):
    df['Optimal Profit'] = df['Mining Price'] - df['Coal Mining Cost']
    return df


# calculate the optimal cost
def calculate_optimal_cost(df):
    df['Optimal Cost'] = df['Coal Mining Cost']
    return df


# Main function read in the coal data and constraints, find the optimal solution and plot the data
def main():
    # read in the coal data
    df = read_data('coal_data.csv')
    # plot the data
    plot_data(df)
    # calculate the profit of each coal
    df = calculate_profit(df)
    # calculate the cost of each coal
    df = calculate_cost(df)
    # read in the constraints
    constraints = read_data('constraints.csv')
    # solve the optimization problem
    x = solve_optimization_problem(df, constraints)
    # calculate the optimal solution
    df = calculate_optimal_solution(df, x)
    # calculate the optimal profit
    df = calculate_optimal_profit(df)
    # calculate the optimal cost
    df = calculate_optimal_cost(df)
    # print the optimal solution
    print(df)

    # Find all the possible solutions
    # 1. Find the optimal solution
    # 2. Find the optimal profit


# Create sample dataset for testing
def create_sample_data():
    df = pd.DataFrame(columns=['Coal Name', 'Coal Mining Quantity', 'Coal Mining Price', 'Coal Mining Cost', 'Profit',
                               'Coal Mining Cost', 'Optimal Solution', 'Optimal Profit', 'Optimal Cost'])
    df.loc[0] = ['Coal 1', 100, 10, 0, 0, 0, 0, 0, 0]
    df.loc[1] = ['Coal 2', 200, 20, 0, 0, 0, 0, 0, 0]
    df.loc[2] = ['Coal 3', 300, 30, 0, 0, 0, 0, 0, 0]
    df.loc[3] = ['Coal 4', 400, 40, 0, 0, 0, 0, 0, 0]
    df.loc[4] = ['Coal 5', 500, 50, 0, 0, 0, 0, 0, 0]
    df.loc[5] = ['Coal 6', 600, 60, 0, 0, 0, 0, 0, 0]
    df.loc[6] = ['Coal 7', 700, 70, 0, 0, 0, 0, 0, 0]
    df.loc[7] = ['Coal 8', 800, 80, 0, 0, 0, 0, 0, 0]
    df.loc[8] = ['Coal 9', 900, 90, 0, 0, 0, 0, 0, 0]
    df.loc[9] = ['Coal 10', 1000, 100, 0, 0, 0, 0, 0, 0]
    return df


# Create sample constraints for testing
def create_sample_constraints():
    constraints = {'A': [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]],
                   'b': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 'c': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
    return constraints


# Test the function
def test():
    # create sample data
    df = create_sample_data()
    # create sample constraints
    constraints = create_sample_constraints()
    # solve the optimization problem
    x = solve_optimization_problem(df, constraints)
    # calculate the optimal solution
    df = calculate_optimal_solution(df, x)
    # calculate the optimal profit
    df = calculate_optimal_profit(df)
    # calculate the optimal cost
    df = calculate_optimal_cost(df)
    # print the optimal solution
    print(df)


# Run the main function
if __name__ == '__main__':
    test()
