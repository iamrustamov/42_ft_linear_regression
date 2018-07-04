#!/usr/bin/python

from __future__ import division
import csv
import math
import matplotlib.pyplot as plt

filename = 'data.csv'
nbIterations = 2000
m = 0
learningRate = 0.01
initialTheta0 = 0.0
initialTheta1 = 0.0
km = []
price = []
errorsCost = []

with open(filename, "rb") as csvfile:
    f = csv.reader(csvfile, delimiter=',')
    for row in f:
        km.append(row[0])
        price.append(row[1])

# delete first row
km.pop(0)
price.pop(0)
m = len(km)

def calcDerivates (theta0, theta1):
    derivateTheta0 = 0.0
    derivateTheta1 = 0.0
    for i in xrange(0, m):
        derivateTheta0 += theta0 + (theta1 * (float(km[i]) / 10000)) - float(price[i])
        derivateTheta1 += (theta0 + (theta1 * (float(km[i]) / 10000)) - float(price[i])) * (float(km[i]) / 10000)
    return [(1 / m) * derivateTheta0, (1 / m) * derivateTheta1]

def updateTheta (theta0, theta1):
    derivate = calcDerivates(theta0, theta1)
    updatedTheta0 = theta0 - (learningRate * derivate[0])
    updatedTheta1 = theta1 - (learningRate * derivate[1])
    errorsCost.append(calcCost(updatedTheta0, updatedTheta1))
    return [updatedTheta0, updatedTheta1]

def gradientDescent ():
    tmpTheta0 = initialTheta0
    tmpTheta1 = initialTheta1
    for i in xrange(0, nbIterations):
        updatedTheta = updateTheta(tmpTheta0, tmpTheta1)
        tmpTheta0 = updatedTheta[0]
        tmpTheta1 = updatedTheta[1]
    return [tmpTheta0, tmpTheta1]

def calcCost (theta0, theta1):
    globalCost = 0
    for i in xrange(0, m):
        globalCost += ((theta0 + (theta1 * (float(km[i]) / 10000))) - float(price[i]) * ((theta0 + (theta1 * (float(km[i]) / 10000))) - float(price[i])))
    return (1 / m) * globalCost

def main():
    finalTheta = gradientDescent()
    print finalTheta[0], finalTheta[1]
    with open('results.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([finalTheta[0], finalTheta[1]])
    plt.plot(km, price, "ro")
    plt.show()

if __name__ == "__main__":
    main()
