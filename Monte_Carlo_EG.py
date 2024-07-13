# got from CHatGPT
import numpy as np
import matplotlib.pyplot as plt

# Define the model: y = a + b * x + noise
a = 5
b = 3
n_simulations = 10000
x_mean = 50
x_std = 10
noise_mean = 0
noise_std = 1

# Generate random samples
x_samples = np.random.normal(x_mean, x_std, n_simulations)
noise_samples = np.random.normal(noise_mean, noise_std, n_simulations)

# Run simulations
y_samples = a + b * x_samples + noise_samples

# Analyze results
mean_y = np.mean(y_samples)
std_y = np.std(y_samples)

# Plot results
plt.hist(y_samples, bins=50, alpha=0.75, edgecolor='black')
plt.title('Monte Carlo Simulation Results')
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.show()

print(f"Mean of outcomes: {mean_y}")
print(f"Standard deviation of outcomes: {std_y}")
