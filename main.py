import numpy as np
import math
import matplotlib.pyplot as plt

def weightFunc(inputVal, weight):
    return inputVal * weight

def computeNeuronOutput(inputs, inputWeigts):
    print(inputs, len(inputs))
    print(inputWeigts, len(inputWeigts))
    if len(inputs) != len(inputWeigts):
        raise ValueError("Arrays must have the same size")
    
    result = 0
    for index, inputVal in enumerate(inputs):
        result += weightFunc(inputVal, inputWeigts[index])
        
    result /= len(inputs)
    return result

def main(argv=None):
    output = computeNeuronOutput([1] * 20, [2] * 20)
    print(output)
    m = 5
    epochs = 0
    cost_history = []
    cost_history.extend( range(1, 20) )
    """plt.plot(cost_history)
    plt.title("The logistic regression cross-entropy cost function"
              + " value, \n"
              + str(m) + " examples, " + str(epochs) + " epochs.")
    plt.xlabel("Epoch");
    plt.ylabel("J(epoch)");
    plt.show()"""
    
if __name__ == "__main__":
    main()
