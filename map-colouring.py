from constraint import Problem

# Create a problem instance
problem = Problem()

# Variables (regions) and their domains (colors)
colors = ['Red', 'Green', 'Blue']
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Add the regions as variables with domain (colors)
problem.addVariables(regions, colors)

# Define the adjacency constraints (neighbors should have different colors)
neighbors = [
    ('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'Q'),
    ('SA', 'Q'), ('SA', 'NSW'), ('SA', 'V'), ('Q', 'NSW'),
    ('NSW', 'V')
]

# Add constraint for each pair of adjacent regions
for region1, region2 in neighbors:
    problem.addConstraint(lambda color1, color2: color1 != color2, (region1, region2))

# Solve the problem
solution = problem.getSolution()

# Print the solution
if solution:
    print("A solution to the Map Coloring Problem is:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found!")
