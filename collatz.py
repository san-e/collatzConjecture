import matplotlib.pyplot as plt
import numpy as np


intList = []

def collatz(startInt, doPrint = True):
    if doPrint:
        print(startInt)
    while True:
        if startInt % 2 != 0:
            intList.append(startInt)
            startInt = int(startInt * 3 + 1)
        else:
            intList.append(startInt)
            startInt = int(startInt / 2)
        if startInt != 1:
            if doPrint:
                print(startInt)
        else:
            if doPrint:
                print(1)
                print("Only looping from here on out, buddy.")
            break;

if __name__ == "__main__":
    startInt = int(input("Select a starting integer: "))
    collatz(startInt = startInt, doPrint = True)

    plt.plot(intList)
    plt.show()