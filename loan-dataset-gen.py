import numpy as np
import pandas as pd
from random import random
import os

# dataset generation
dataset = pd.DataFrame(columns=["reputation", "lenght", "income", "y"])
n = 40
for i in range(n):
    reputation = np.random.randint(0,3)
    if reputation == 0:
        reputation = "excellent"
    elif reputation == 1:
        reputation = "good"
    else: reputation = "bad"

    lenght = np.random.randint(1,3)
    lenght = 2*lenght + 1
    
    income = np.random.randint(0,2)
    if income == 0: income = "high"
    else: income = "modest"

    r = random()
    if reputation == "excellent" and lenght == 5 and income == "high":
        if r<0.95: y = "safe"
        else: y = "risky"
    elif reputation == "excellent" and lenght == 5 and income == "modest":
        if r<0.8: y = "safe"
        else: y = "risky"
    elif reputation == "excellent" and lenght == 3 and income == "high":
        if r<0.9: y = "safe"
        else: y = "risky"
    elif reputation == "excellent" and lenght == 3 and income == "modest":
        if r<0.7: y = "safe"
        else: y = "risky"
    elif reputation == "good" and lenght == 5 and income == "high":
        if r<0.7: y = "safe"
        else: y = "risky"
    elif reputation == "good" and lenght == 5 and income == "modest":
        if r<0.5: y = "safe"
        else: y = "risky"
    elif reputation == "good" and lenght == 3 and income == "high":
        if r<0.5: y = "safe"
        else: y = "risky"
    elif reputation == "good" and lenght == 3 and income == "modest":
        if r<0.35: y = "safe"
        else: y = "risky"
    elif reputation == "bad" and lenght == 5 and income == "high":
        if r<0.4: y = "safe"
        else: y = "risky"
    elif reputation == "bad" and lenght == 5 and income == "modest":
        if r<0.15: y = "safe"
        else: y = "risky"
    elif reputation == "bad" and lenght == 3 and income == "high":
        if r<0.1: y = "safe"
        else: y = "risky"
    elif reputation == "bad" and lenght == 3 and income == "modest":
        if r<0.05: y = "safe"
        else: y = "risky"
    
    dataset.loc[i] = [reputation, lenght, income, y]

path = os.getcwd()
dataset.to_csv("loan.csv", index=False)