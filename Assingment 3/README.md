# Assignment 4: Probability and Statistics

This assignment covers fundamental concepts in probability and statistics through practical Python implementations and simulations.

## Contents

- **probability_statistics_assignment.ipynb**: Complete Jupyter Notebook with all 6 problems and detailed explanations

## Topics Covered

### 1. Basics of Probability
- Coin toss simulation (10,000 trials)
- Dice rolling probability (sum of 7)
- Experimental vs. theoretical probability

### 2. Multiple Trials
- Probability of getting at least one "6" in 10 die rolls
- Compound probability calculations

### 3. Conditional Probability and Bayes' Theorem
- Drawing colored balls with replacement
- Calculating conditional probabilities
- Verifying independence with Bayes' theorem

### 4. Discrete Random Variables
- Sampling from discrete distributions
- Computing empirical mean, variance, and standard deviation
- Comparing empirical vs. theoretical statistics

### 5. Continuous Random Variables
- Exponential distribution simulation
- Histogram visualization
- PDF (Probability Density Function) overlay

### 6. Central Limit Theorem
- Demonstration of CLT with uniform distribution
- Sample means distribution
- Visualization of normality emergence

## Required Libraries

```python
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
```

## How to Use

1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook probability_statistics_assignment.ipynb
   ```

2. Run all cells sequentially to see the simulations and visualizations

3. Each problem includes:
   - Detailed explanation of the concept
   - Well-documented Python code
   - Output showing experimental results
   - Comparison with theoretical values
   - Visualizations (where applicable)

## Key Learning Outcomes

- Understanding experimental vs. theoretical probability
- Applying Python's `random` and `numpy` modules for simulations
- Computing conditional probabilities
- Working with discrete and continuous probability distributions
- Visualizing statistical concepts with matplotlib
- Understanding and demonstrating the Central Limit Theorem

## Notes

- All simulations use random sampling, so results will vary slightly each time
- The larger the number of trials, the closer experimental results approach theoretical values
- Visualizations help build intuition about probability distributions
