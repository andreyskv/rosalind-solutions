# Mortal Fibonacci Rabbits

N = 89;  # Number of months
M = 16;  # Mortality after # months
K = 1;  # Reproduction rate per month (1 matches Fibonacci seq)

p = [0, 1]  # Population p0 is aged 0, p1 is aged 1(newborns), p2 is aged 2 etc
for n in range(1, N):
    nb = K * sum(p[2:])  # Create newborns
    p.insert(0, 0)       # Add a new generation layer
    p[1] = nb            # Set newborns to the p1 layer
    p = p[:M + 1]        # Old rabbits die (i.e remove last layer(s))
    print(p[:])          # Distribution by generation

print(sum(p[:]))         # Total number of rabbits in the end
