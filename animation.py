import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import random


x_vals = []
y_vals = []

colours = ['red', 'green', 'red', 'blue', 'black', 'yellow', 'yellow']


gradient = int(input("Input the Gradient, you can make it as large as you want but then you won't see anything happen: \t"))
def get_intercept():
    intercept = int(input("Input the Y-Intercept, it must be positive and within the range of 0 to 10000"))
    if intercept > 10000 or intercept < 0:
        print("That is outside of the specified range")
        intercept = get_intercept()
    return intercept

def get_randomness():
    randomness = int(input("Please enter a randomness between 100 and 5000"))
    if randomness > 10000 or randomness < 0:
        print("That does not meet the requirements.")
        randomness = get_randomness()
    return randomness

randomness = get_randomness()

intercept = get_intercept()
reg = LinearRegression()

for i in range(1, 10000):
    if i % 200 == 0:
        plt.clf()
        x_vals.append(random.randint(i,( i+randomness)))
        y_vals.append((random.randint(i,( i+randomness))*gradient)+intercept)
        x = np.array(x_vals)
        x = x.reshape(-1, 1)
        y = np.array(y_vals)
        y = y.reshape(-1, 1)
        reg.fit(x, y)
        plt.xlim(0, 30000)
        plt.ylim(0, 30000)
        plt.scatter(x_vals, y_vals, color = random.choice(colours))
        plt.plot(list(range(15000)), reg.predict(np.array([x for x in range(15000)]).reshape(-1,1)), color = random.choice(colours))
        plt.pause(0.00001)


    if i % 100 == 0:
        if not random.randint(0, 100) > 90:
            x_vals.append(random.randint(i,( i+randomness)))
            y_vals.append((random.randint(i,( i+randomness))*gradient)+intercept)
        else:
            x_vals.append(random.randint((i+500), (i+7000)))
            y_vals.append((random.randint((i+2000), (i+7000))*gradient)+intercept)


        plt.xlim(0, 15000)
        plt.ylim(0, 15000)
        plt.scatter(x_vals, y_vals, color = random.choice(colours))
        plt.pause(0.00001)        
    

plt.show()


if gradient > 10:
    print("SEE I TOLD YOU IT WOULDN'T WORK")






