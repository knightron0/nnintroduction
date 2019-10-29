import numpy as np

def train(self, data, all_y_values):
    learn_rate = 0.1
    epochs = 1000
    
    for epoch in range(epochs):
        