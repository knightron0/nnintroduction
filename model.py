import numpy as np
import neuron


class neuralnetwork:
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0

        self.h1 = neuron.Neuron(weights, bias)
        self.h2 = neuron.Neuron(weights, bias)
        self.o1 = neuron.Neuron(weights, bias)

    def feedforwar(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1

network = neuralnetwork()
x = np.array([2, 3])
print(network.feedforwad(x)) 
        