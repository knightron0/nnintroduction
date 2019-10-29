import numpy as np

def mse_loss(yt, yp):
    return ((yt-yp)**2).mean()

