#MapPlot.py
#Name: Jacob O
#Date: 4/19
#Assignment: Lab 10

# Added three visualizations for Vehicle dataset: Horsepower vs City MPG, Horsepower vs Highway MPG, and City MPG vs Highway MPG. SEE COMMENT ON CANVAS FOR EXPLANATION OF GRAFS.

import matplotlib.pyplot as plt
import numpy as np

import cars 
data = cars.get_car()

city_mpg = []
highway_mpg = []
horsepower = []

for car in data:
    try:
        city = car['Fuel Information']['City mpg']
        highway = car['Fuel Information']['Highway mpg']
        hp = car['Engine Information']['Engine Statistics']['Horsepower']

        if city == 0 or highway == 0 or hp == 0:
            continue
        if city > 100 or highway > 100:
            continue

        city_mpg.append(city)
        highway_mpg.append(highway)
        horsepower.append(hp)

    except KeyError:
        continue

# Set up the figure size
plt.figure(figsize=(18, 5))  # width, height in inches

# Subplot 1: Horsepower vs City MPG
plt.subplot(1, 3, 1)  # 1 row, 3 columns, 1st plot
plt.scatter(horsepower, city_mpg, alpha=0.5, color='blue')
plt.xlabel('Horsepower')
plt.ylabel('City MPG')
plt.title('Horsepower vs City MPG')
plt.grid(True)

# Subplot 2: Horsepower vs Highway MPG
plt.subplot(1, 3, 2)  # 1 row, 3 columns, 2nd plot
plt.scatter(horsepower, highway_mpg, alpha=0.5, color='green')
plt.xlabel('Horsepower')
plt.ylabel('Highway MPG')
plt.title('Horsepower vs Highway MPG')
plt.grid(True)

# Subplot 3: City MPG vs Highway MPG
plt.subplot(1, 3, 3)  # 1 row, 3 columns, 3rd plot
plt.scatter(city_mpg, highway_mpg, alpha=0.5, color='purple')
plt.xlabel('City MPG')
plt.ylabel('Highway MPG')
plt.title('City MPG vs Highway MPG')
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Show all three plots together
plt.savefig("vehicle_mpg_relationships.png")
plt.show()
