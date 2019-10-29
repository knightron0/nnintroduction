import numpy as np
import model

data = np.array([
  [-2, -1],
  [25, 6], 
  [17, 4], 
  [-15, -6],
])
all_y_trues = np.array([
  1,
  0,
  0,
  1,
])

network = model.neuralnetwork()
network.train(data, all_y_trues)

emily = np.array([-7, -3])
frank = np.array([2, 3])
print("Emily: %.3f" % network.feedforward(emily)) 
print("Frank: %.3f" % network.feedforward(frank))