import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import random


x_vals = []
y_vals = []




gradient = float(input("Input the Gradient, you can make it as large as you want but then you won't see anything happen: \n"))
def get_intercept():
    intercept = float(input("Input the Y-Intercept, it must be positive and within the range of 0 to 5000:\n"))
    if intercept > 5000 or intercept < 0:
        print("That is outside of the specified range")
        intercept = get_intercept()
    return intercept

def get_randomness():
    randomness = float(input("Please enter a randomness between 100 and 5000: \n"))
    if randomness > 5001 or randomness < 0:
        print("That does not meet the requirements.")
        randomness = get_randomness()
    return randomness

randomness = get_randomness()

intercept = get_intercept()
reg = LinearRegression()

for i in range(1, 10000):
    if i % 200 == 0:
        plt.clf()
        x_vals.append(random.randint(i,( i+100)))
        y_vals.append((random.randint(i,( i+randomness))*gradient)+intercept)
        x = np.array(x_vals)
        x = x.reshape(-1, 1)
        y = np.array(y_vals)
        y = y.reshape(-1, 1)
        reg.fit(x, y)
        plt.xlim(0, 20000)
        plt.ylim(0, 20000)
        plt.scatter(x_vals, y_vals, color = 'red')
        plt.plot(list(range(15000)), reg.predict(np.array([x for x in range(15000)]).reshape(-1,1)), color = 'red')
        plt.pause(0.0001)


    if i % 100 == 0:
        if not random.randint(0, 100) > 90:
            x_vals.append(random.randint(i,( i+100)))
            y_vals.append((random.randint(i,( i+randomness))*gradient)+intercept)
        else:
            x_vals.append(random.randint((i), (i+100)))
            y_vals.append((random.randint((i+2000), (i+7000))*gradient)+intercept)


        plt.xlim(0, 20000)
        plt.ylim(0, 20000)
        plt.scatter(x_vals, y_vals, color = 'red')
        plt.pause(0.0001)        
    

plt.show()


if gradient > 10:
    print("SEE I TOLD YOU IT WOULDN'T WORK")






